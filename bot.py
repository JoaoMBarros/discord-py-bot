import os
from decouple import config
from discord.ext import commands

bot = commands.Bot('canacchi ')

def load_cogs(bot):
    bot.load_extension('listeners.greetings')
    bot.load_extension('listeners.meme')
    bot.load_extension('tasks.jokenpo')

    for file in os.listdir("Bot/commands/"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

load_cogs(bot)

TOKEN = config("TOKEN")
bot.run(TOKEN)