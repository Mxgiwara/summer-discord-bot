import discord
from discord import app_commands
from param import intents, client, tree

@client.event
async def on_guild_join(guild: discord.Guild):
    await guild.create_role(name="muted")
    role = "muted"
    for channel in guild.channels:
            await channel.set_permissions(role, send_messages=False)