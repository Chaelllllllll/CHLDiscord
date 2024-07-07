import discord
import requests
import json

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Enable message content intent

client = discord.Client(intents=intents)

# Load the token from the config.json file
with open('config.json') as config_file:
    config = json.load(config_file)
TOKEN = config['DISCORD_BOT_TOKEN']

# API endpoint
API_URL = 'https://markdevs-api.onrender.com/api/gpt4o'

def get_api_response(prompt_input):
    data = {'q': prompt_input}
    try:
        response = requests.get(API_URL, params=data)
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get('status'):
                return response_json['response']
            else:
                return "Failed to get response."
        else:
            return "Failed to get response."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ask'):
        prompt_input = message.content[len('!ask '):].strip()
        if prompt_input:
            response = get_api_response(prompt_input)
            if len(response) > 2000:
                for i in range(0, len(response), 2000):
                    await message.channel.send(response[i:i+2000])
            else:
                await message.channel.send(response)
        else:
            await message.channel.send("Please provide a prompt after the command.")

client.run(TOKEN)
