import discord
from discord import app_commands
from param import intents, client, tree

@tree.command(name='ping', description='return pong')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('pong')


