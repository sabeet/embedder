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


@client.event
async def on_ready():
    print('Embedder is now running')


def is_tiktok_url(url):
    netloc = urlparse(url).netloc.lower()
    return netloc in ["tiktok.com"] or netloc.startswith("www.tiktok.com")


def is_instagram_url(url):
    netloc = urlparse(url).netloc.lower()
    return netloc in ["instagram.com"] or netloc.startswith("www.instagram.com")


def is_twitter_url(url):
    netloc = urlparse(url).netloc.lower()
    return netloc in ["x.com", "twitter.com"] or netloc.startswith("www.x.com") or netloc.startswith("www.twitter.com")


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
        if is_tiktok_url(url):
            updated_url = url.replace("tiktok.com", "vxtiktok.com")
            urls_found.append(updated_url)
        elif is_instagram_url(url):
            updated_url = url.replace("instagram.com", "kkinstagram.com")
            urls_found.append(updated_url)
        elif is_twitter_url(url):
            if "x.com" in url:
                updated_url = url.replace("x.com", "fxtwitter.com")
                urls_found.append(updated_url)
            elif "twitter.com" in url:
                updated_url = url.replace("twitter.com", "fxtwitter.com")
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
