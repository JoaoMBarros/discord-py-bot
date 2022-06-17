import discord

from discord.ext import commands

class Talks(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fala")
    async def send_message(ctx):
        name = ctx.author.name
        response = "muito boa tarde " + name
        await ctx.send(response)


def setup(bot):
    bot.add_cog(Talks(bot))