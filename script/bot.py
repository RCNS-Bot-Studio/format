from config import PointConfig
from discord import Interaction, Object
from discord.ext import commands

bot = commands.Bot(command_prefix=PointConfig.prefix, intents=PointConfig.intents())


@bot.event
async def on_ready():
    bot.tree.copy_global_to(guild=Object(id=PointConfig.guild_id))
    await bot.tree.sync(guild=Object(id=PointConfig.guild_id))


@bot.command(name="핑")
async def content_ping(ctx: commands.Context) -> None:
    return await ctx.send("퐁")


@bot.tree.command(name="핑", description="퐁을 대답합니다.")
async def slash_ping(inter: Interaction) -> None:
    return await inter.response.send_message("퐁")


bot.run(PointConfig.token)
