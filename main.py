import discord
import os
from discord import app_commands
from dotenv import load_dotenv
from param import intents, client, tree
import commands_ping
import moderation
import event    


try:
    load_dotenv()

    token = os.getenv('DISCORD_TOKEN')
    owner = os.getenv('OWNER_ID')

    @client.event
    async def on_connect():
        print(f"Bot connected successfully to discord")

    @client.event
    async def on_ready():
        await tree.sync()
        print(f"Logged in as {client.user}.")
        user = await client.fetch_user(int(owner))
        await user.send("Bot successfully connected")
    
    client.run(token)

except Exception as e:
    print(f"{e}")

