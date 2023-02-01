from discord.ext import commands

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='canaping')
    async def send_canaping_image(self, ctx):
        image = 'https://imgur.com/dADlyIv'
        await ctx.message.delete()
        await ctx.send(image)

async def setup(bot):
    await bot.add_cog(Images(bot))