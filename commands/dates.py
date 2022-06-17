from datetime import datetime
from discord.ext import commands

class Dates(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Dates(bot))