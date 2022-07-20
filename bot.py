import os
from decouple import config
from discord.ext import commands

bot = commands.Bot('canacchi ')

def load_cogs(bot):

    for file in os.listdir("listeners/"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

    for file in os.listdir("commands/"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

    for file in os.listdir("tasks/"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

load_cogs(bot)

TOKEN = config("TOKEN")
bot.run(TOKEN)