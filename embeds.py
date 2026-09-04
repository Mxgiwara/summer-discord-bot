import discord
from embeds_dict import color_dict, title_dict, text_dict

def embed_ban(choice: str):
    if choice == "fail":
        embed_ban_failed = discord.Embed(
            color=color_dict.get("failed"),
            title=title_dict.get("ban")
        )
        embed_ban_failed.add_field(name=text_dict.get("ban_failed"), value="")
        return embed_ban_failed
    
    elif choice == "success":

        embed_ban_successfull = discord.Embed(
            color=color_dict.get("success"),
            title=title_dict.get("ban")
        )
        embed_ban_successfull.add_field(name=text_dict.get("ban_successful"), value="")
        return embed_ban_successfull

embed_mute_failed = discord.Embed(
    color=color_dict.get("fail"),
    title=title_dict.get("mute")
)

embed_mute_success = discord.Embed(
    color=color_dict.get("success"),
    title=title_dict.get("mute")
)

