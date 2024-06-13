import discord
import requests
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = 'TOKEN'
CHANNEL_ID = CHANNEL_ID

client = discord.Client(intents=discord.Intents.default())

async def get_public_ip():
    try:
        logging.info('Fetching public IP...')
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        ip = response.json().get('ip')
        logging.info(f'Current public IP: {ip}')
        return ip
    except requests.RequestException as e:
        logging.error(f'Error fetching IP: {e}')
        return None

async def check_ip_change():
    previous_ip = None
    while True:
        current_ip = await get_public_ip()
        if current_ip:
            if current_ip != previous_ip:
                channel = client.get_channel(CHANNEL_ID)
                if channel:
                    try:
                        logging.info(f'Sending IP change message to channel: {current_ip}')
                        await channel.send(f'Public IP has changed: {current_ip}')
                        previous_ip = current_ip
                    except discord.DiscordException as e:
                        logging.error(f'Error sending message to channel: {e}')
                else:
                    logging.error(f'Could not find the channel with ID {CHANNEL_ID}. Make sure the ID is correct and the bot has access to this channel.')
            else:
                logging.info('IP has not changed.')
        else:
            logging.error('Could not retrieve the current IP.')
        await asyncio.sleep(60)  # Check every 1 minute for testing purposes

async def send_test_message():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        try:
            logging.info('Sending test message to channel.')
            await channel.send('Bot is online and ready to monitor IP changes.')
        except discord.DiscordException as e:
            logging.error(f'Error sending test message to channel: {e}')
    else:
        logging.error(f'Could not find the channel with ID {CHANNEL_ID}. Make sure the ID is correct and the bot has access to this channel.')

@client.event
async def on_ready():
    logging.info(f'Logged in as {client.user} (ID: {client.user.id})')
    await send_test_message()
    client.loop.create_task(check_ip_change())

client.run(TOKEN)