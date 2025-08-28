import os
import nest_asyncio
from urllib.parse import urlparse
import discord
import re
from dotenv import load_dotenv

nest_asyncio.apply()
load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

url_map = {
    "tiktok.com": "www.vxtiktok.com",
    "instagram.com": "www.kkinstagram.com",
    "x.com": "www.fxtwitter.com",
    "twitter.com": "www.fxtwitter.com",
}

@client.event
async def on_ready():
    print('Embedder is now running')

def extract_urls(text):
    # Extract URLs from text using regex to handle markdown and other formatting
    url_pattern = r'https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?)?'
    return re.findall(url_pattern, text)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Extract URLs using regex instead of splitting by spaces
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
