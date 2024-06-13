# Discord IP Monitor Bot

This Discord bot monitors your public IP address and sends a message to a specified Discord channel if the IP address changes.

## Requirements

- Python 3.6 or higher
- `discord.py` library
- `requests` library

## Installation

1. Clone the repository or download the `ip_bot.py` script.
2. Install the required libraries:

    ```sh
    pip install discord.py requests
    ```

## Configuration

1. Replace `YOUR_DISCORD_BOT_TOKEN` in the script with your actual Discord bot token.
2. Replace `YOUR_DISCORD_CHANNEL_ID` with the ID of the Discord channel where you want to send the messages.

## Usage

Run the bot with the following command:

```sh
python ip_bot.py
