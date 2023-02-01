import os
import discord
import asyncio
from decouple import config
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='canacchi ', intents=intents)

TOKEN = config("TOKEN")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

async def load_cogs():
    await bot.load_extension('listeners.greetings')
    await bot.load_extension('listeners.meme')
    await bot.load_extension('listeners.ia')
    await bot.load_extension('tasks.jokenpo')
    await bot.load_extension('tasks.hangman')

    for file in os.listdir("commands/"):
        if file.endswith(".py"):
            #await bot.load_extension(f'cogs.{file[:-3]}')
            cog = file[:-3]
            await bot.load_extension(f"commands.{cog}")

asyncio.run(main())