from discord.ext import commands

class Channels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='canaltivra')
    async def send_message_canaltivra(self, ctx):
        response = 'https://www.youtube.com/channel/UCQsuIHnEo4Iiex3NoeXAfAQ'
        await ctx.send(response)

    @commands.command(name='ginnews')
    async def send_message_ginnews(self, ctx):
        response = 'https://www.youtube.com/channel/UCbMHRGt0u8MaVo89P-ZoNJw'
        await ctx.send(response)
    
    @commands.command(name = "ssreviewers")
    async def send_message_ssreviewers(self, ctx):
        print(ctx.message.attachments[0].url)
        response = 'https://www.youtube.com/channel/UCqy7pIHxn_i9iF-j2PPw2sg'
        await ctx.send(response)

def setup(bot):
    bot.add_cog(Channels(bot))
