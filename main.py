import os
import nest_asyncio
from urllib.parse import urlparse, urlunparse
import discord
from dotenv import load_dotenv

nest_asyncio.apply()
load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

url_map = {
    "tiktok.com": "vxtiktok.com",
    "instagram.com": "kkinstagram.com",
    "x.com": "fxtwitter.com",
    "twitter.com": "fxtwitter.com",
}

@client.event
async def on_ready():
    print('Embedder is now running')

# Extract URLs using urlparse and checking if there is a scheme and netloc
def extract_urls(text):
    urls = []
    split_text = text.split()

    for t in split_text:
        parsed = urlparse(t)
        if parsed.scheme and parsed.netloc:
            urls.append(t)

    return urls


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    urls_in_message = extract_urls(message.content)
    urls_found = []

    for url in urls_in_message:
        for oldUrl, newUrl in url_map.items():
            netloc = urlparse(url).netloc.lower()
            if netloc in oldUrl or netloc.startswith("www." + oldUrl): 
                updated_url = url.replace(oldUrl, newUrl)
                urls_found.append(updated_url)

    if urls_found:
        # Send all updated URLs as a reply without mentioning the user
        urls_text = "\n".join(urls_found)
        await message.reply(urls_text, mention_author=False)

        # Remove embeds from the original message
        try:
            await message.edit(suppress=True)
        except discord.Forbidden:
            print(f"Missing permissions to suppress embeds in #{message.channel.name}")
        except discord.HTTPException as e:
            print(f"Failed to suppress embeds: {e}")


client.run(TOKEN)
