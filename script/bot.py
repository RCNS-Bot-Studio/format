from config import PointConfig
from discord import Object
from discord.ext import commands

bot = commands.Bot(command_prefix=PointConfig.prefix, intents=PointConfig.intents())


@bot.event
async def on_ready():
    bot.tree.copy_global_to(guild=Object(id=PointConfig.guild_id))
    await bot.tree.sync(guild=Object(id=PointConfig.guild_id))


bot.run(PointConfig.token)
