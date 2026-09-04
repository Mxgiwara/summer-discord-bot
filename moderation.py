import discord
import discord.ext
import asyncio
from discord import app_commands
from param import intents, client, tree
import embeds as emb


@tree.command(name='ban', description='ban a member')
@app_commands.default_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, user: discord.User, reason:str):
    if user.name == client.user.name:
        embed_ban = emb.embed_ban("failed")
        await interaction.response.send_message(embed=embed_ban)
        return
    
    if user.name == interaction.user.name:
        emb.embed_ban_failed.add_field(name='❌Ban failed!', value="You cannot ban yourself !")
        await interaction.response.send_message(embed=emb.embed_ban_failed)
        return
    
    if not interaction.user.guild_permissions.ban_members:
        emb.embed_ban_failed.add_field(name='❌Ban failed!', value="You don't have the permission to ban members")
        await interaction.response.send_message(embed=emb.embed_ban_failed)

    else:
        await interaction.guild.ban(user=user, reason=reason)
        await interaction.response.send_message(f"{user.name} has been banned by {interaction.user.name}!\nReason: {reason}")

@tree.command(name='unban', description='unban an user')
@app_commands.default_permissions(ban_members=True)

async def unban(interaction: discord.Interaction, user: discord.User, reason:str):
    async for ban_entry in interaction.guild.bans():
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message(f"You don't have the permission to unban members")

        if ban_entry.user == user:
            await interaction.guild.unban(user=user, reason=reason)
            await interaction.response.send_message(f"{user.name} has been unbanned !\n Reason: {reason}")

        else:
            await interaction.response.send_message(f"This user isn't banned")
            break

@tree.command(name='mute', description='mute a member')
@app_commands.default_permissions(manage_messages=True)

async def mute(interaction: discord.Interaction, member: discord.Member, duration: float, reason:str,):
    if not interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message(f"You don't have the permission to mute members")
    
    else:
        try:
            role = discord.utils.get(interaction.guild.roles, name = 'muted')

            if not role is None :
                await member.add_roles(role)
                await interaction.response.send_message(f"{member.name} has been muted for {duration} minutes")
                await asyncio.sleep(duration*60)
                await member.remove_roles(role)
                await interaction.channel.send(f"{member.name} is unmuted !")
                
            else:
                await interaction.guild.create_role(name='muted')
                role = discord.utils.get(interaction.guild.roles, name = 'muted')
                for channel in interaction.guild.channels:
                    await channel.set_permissions(role, send_messages=False)
                    await member.add_roles(role)

                await member.add_roles(role)
                await interaction.response.send_message(f"{member.name} has been muted for {duration} minutes")
                await asyncio.sleep(duration*60)
                await member.remove_roles(role)
                await interaction.channel.send(f"{member.name} is unmuted !")
        
        except Exception as e:
            print(f"The error is {e}")

@tree.command(name='unmute', description='unmute a member')
@app_commands.default_permissions(manage_messages=True)

async def unmute(interaction: discord.Interaction, member: discord.Member):
    role = discord.utils.get(member.roles, name = 'muted')
    if role:
        await member.remove_roles(role)
        await interaction.response.send_message(f"{member.name} has been unmuted by {interaction.user.name}!")

    else:
        await interaction.response.send_message(f"This member has not been muted !")

    
        
            

