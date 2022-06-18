# Adicionar o default no jokenpo
# Melhorar os ifs encadeados no jokenpo
# Colocar na partida de jokenpo só quem foi pingado
# Arrumar o timing do jokenpo (contagem muito rapida) 

import os
from decouple import config
from discord.ext import commands

bot = commands.Bot('canacchi ')

def load_cogs(bot):
    bot.load_extension('listeners.greetings')
    bot.load_extension('tasks.jokenpo')

    for file in os.listdir("commands/"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

load_cogs(bot)

TOKEN = config("TOKEN")
bot.run(TOKEN)