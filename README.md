# Discord Video Embedder Bot

A Discord bot that automatically converts social media links to their embeddable equivalents, allowing videos to be watched directly within Discord without needing to open external links.

## Features

- **Automatic Link Conversion**: Detects social media links in messages and converts them to embeddable formats
- **Embed Suppression**: Removes the original non-embeddable previews to keep chat clean
- **Multi-Platform Support**: Currently supports TikTok, Instagram, and Twitter/X links
- **Smart URL Detection**: Uses regex to find URLs even within markdown formatting and other text

## Supported Platforms

| Platform | Original Domain | Converted Domain | Status |
|----------|----------------|------------------|---------|
| TikTok | `tiktok.com` | `vxtiktok.com` | ✅ Active |
| Instagram | `instagram.com` | `kkinstagram.com` | ✅ Active |
| Twitter/X | `twitter.com` / `x.com` | `fxtwitter.com` | ✅ Active |

## How It Works

1. **Detection**: The bot monitors all messages in channels it has access to
2. **URL Extraction**: Uses regex pattern matching to find social media URLs in messages
3. **Conversion**: Replaces the original domains with embeddable alternatives:
   - `tiktok.com` → `vxtiktok.com`
   - `instagram.com` → `kkinstagram.com`
   - `twitter.com` or `x.com` → `fxtwitter.com`
4. **Response**: Replies with the converted links (without mentioning the original poster)
5. **Cleanup**: Attempts to suppress the original message's embeds to avoid duplication

## Installation

### Prerequisites

- Python 3.8 or higher
- A Discord bot token

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd discord-video-embedder
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   Create a `.env` file in the project root:
   ```env
   echo "TOKEN=your_discord_bot_token_here" > .env
   ```

4. **Run the bot**
   ```bash
   python main.py
   ```

## Requirements

The bot requires the following Python packages (see `requirements.txt`):

- `discord.py` - Discord API wrapper
- `python-dotenv` - Environment variable management
- `nest_asyncio` - Asyncio compatibility for nested event loops

## Bot Permissions

The bot requires the following Discord permissions:

- **Read Messages** - To detect URLs in chat
- **Send Messages** - To reply with converted links
- **Manage Messages** - To suppress original embeds (optional)

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `TOKEN` | Your Discord bot token | Yes |

### Bot Intents

The bot uses the following Discord intents:
- Default intents
- Message content intent (to read message text)

## Usage

Once the bot is running and added to your server:

1. Post a message containing a TikTok, Instagram, or Twitter/X link
2. The bot will automatically reply with the embeddable version
3. The original message's preview will be suppressed (if the bot has permissions)

### Example

**User posts:**
```
Check out this cool video! https://www.tiktok.com/@user/video/1234567890
```

**Bot replies:**
```
https://vxtiktok.com/@user/video/1234567890
```

The converted link will show a proper video embed that can be played directly in Discord.

## Error Handling

- **Permission Errors**: If the bot lacks permission to suppress embeds, it will log the error but continue functioning
- **HTTP Exceptions**: Network-related errors are caught and logged
- **Invalid URLs**: Non-matching URLs are ignored without errors

## Contributing

Feel free to submit issues or pull requests to add support for additional platforms or improve functionality.

## Limitations

- The bot relies on third-party services (vxtiktok.com, kkinstagram.com, fxtwitter.com) for embedding
- Embed suppression requires "Manage Messages" permission
- Some private or restricted content may not embed properly even with converted links

## License

This project is open source and available under the MIT License.
