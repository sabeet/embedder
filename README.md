# Discord Video Embedder Bot

A Discord bot that automatically converts social media links to their embeddable equivalents, allowing videos to be watched directly within Discord without needing to open external links.

## Features

- **Automatic Link Conversion**: Detects social media links in messages and converts them to embeddable formats
- **Embed Suppression**: Removes the original non-embeddable previews to keep chat clean
- **Multi-Platform Support**: Currently supports TikTok, Instagram, and Twitter/X links
- **Smart URL Detection**: Uses Python's built-in URL parsing library to find URLs even within markdown formatting and other text
- **Docker Support**: Easy deployment with Docker and Docker Compose

## Supported Platforms

| Platform | Original Domain | Converted Domain | Status |
|----------|----------------|------------------|---------|
| TikTok | `tiktok.com` | `vxtiktok.com` | ✅ Active |
| Instagram | `instagram.com` | `kkinstagram.com` | ✅ Active |
| Twitter/X | `twitter.com` / `x.com` | `fxtwitter.com` | ✅ Active |

## How It Works

1. **Detection**: The bot monitors all messages in channels it has access to
2. **URL Extraction**: Uses URL parsing to find social media URLs in messages
3. **Conversion**: Replaces the original domains with embeddable alternatives:
   - `tiktok.com` → `vxtiktok.com`
   - `instagram.com` → `kkinstagram.com`
   - `twitter.com` or `x.com` → `fxtwitter.com`
4. **Response**: Replies with the converted links (without mentioning the original poster)
5. **Cleanup**: Attempts to suppress the original message's embeds to avoid duplication

## Installation

### Prerequisites

- Python 3.8 or higher OR Docker
- A Discord bot token ([Get one here](https://discord.com/developers/applications))

### Option 1: Docker Deployment (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/sabeet/embedder.git
   cd embedder
   ```

2. **Create environment file**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Discord bot token:
   ```env
   TOKEN=your_discord_bot_token_here
   ```

3. **Run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

4. **View logs**
   ```bash
   docker-compose logs -f
   ```

5. **Stop the bot**
   ```bash
   docker-compose down
   ```

### Option 2: Manual Docker Commands

```bash
# Build the image
docker build -t embedder .

# Run the container
docker run -d --name embedder-bot -e TOKEN="your_token_here" embedder
```

### Option 3: Python (Local Development)

1. **Clone the repository**
   ```bash
   git clone https://github.com/sabeet/embedder.git
   cd embedder
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variable**
   
   **Linux/Mac:**
   ```bash
   export TOKEN="your_discord_bot_token_here"
   ```
   
   **Windows (PowerShell):**
   ```powershell
   $env:TOKEN="your_discord_bot_token_here"
   ```

4. **Run the bot**
   ```bash
   python main.py
   ```

## Portainer Deployment

For deployment to Portainer as a stack:

1. Copy the contents of `docker-compose.yml`
2. Create a new stack in Portainer
3. Paste the compose file
4. Add environment variable:
   - Name: `TOKEN`
   - Value: `your_discord_bot_token_here`
5. Deploy the stack

Alternatively, pull the pre-built image from Docker Hub:

```yaml
version: '3.8'

services:
  embedder:
    image: sabeet/embedder:latest
    container_name: embedder-bot
    restart: unless-stopped
    environment:
      - TOKEN=${TOKEN} # You must get a discord bot token from the Discord Developer Portal
```

## Requirements

The bot requires the following Python packages (see `requirements.txt`):

- `discord.py` - Discord API wrapper
- `nest_asyncio` - Asyncio compatibility for nested event loops

## Bot Permissions

The bot requires the following Discord permissions:

- **Read Messages** - To detect URLs in chat
- **Send Messages** - To reply with converted links
- **Manage Messages** - To suppress original embeds (optional but recommended)

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `TOKEN` | Your Discord bot token | Yes |

### Bot Intents

The bot uses the following Discord intents:
- Default intents
- Message content intent (must be enabled in Discord Developer Portal)

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

## Docker Hub

Pre-built images are available on Docker Hub:
```bash
docker pull sabeet/embedder:latest
```

## Error Handling

- **Permission Errors**: If the bot lacks permission to suppress embeds, it will log the error but continue functioning
- **HTTP Exceptions**: Network-related errors are caught and logged
- **Invalid URLs**: Non-matching URLs are ignored without errors

## Troubleshooting

- **Bot not responding**: Ensure the Message Content intent is enabled in Discord Developer Portal
- **TOKEN not set error**: Verify your environment variable is properly configured
- **Permission errors**: Grant the bot "Manage Messages" permission in your server

## Contributing

Feel free to submit issues or pull requests to add support for additional platforms or improve functionality.

## Limitations

- The bot relies on third-party services (vxtiktok.com, kkinstagram.com, fxtwitter.com) for embedding
- Embed suppression requires "Manage Messages" permission
- Some private or restricted content may not embed properly even with converted links

## License

This project is open source and available under the MIT License.