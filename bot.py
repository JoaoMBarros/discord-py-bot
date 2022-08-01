import os
from decouple import config
from discord.ext import commands

bot = commands.Bot('canacchi ')

def load_cogs(bot):
    bot.load_extension('listeners.greetings')
    bot.load_extension('listeners.meme')
    bot.load_extension('tasks.jokenpo')
    bot.load_extension('tasks.hangman')
#    bot.load_extension('tasks.bingo')
#    bot.load_extension('tasks.teste')
#    bot.load_extension('tasks.bet')

    for file in os.listdir("commands/"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")
load_cogs(bot)

TOKEN = config("TOKEN")
bot.run(TOKEN)