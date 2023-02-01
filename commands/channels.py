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
        response = 'https://www.youtube.com/channel/UCqy7pIHxn_i9iF-j2PPw2sg'
        await ctx.send(response)
    
    @commands.command(name='fecharcanal')
    async def close_channel(self, ctx):
        if ctx.message.author.id != 193296310525231114:
            return
            
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.message.delete()

        await ctx.send('Chat fechado', delete_after=2.0)

    @commands.command(name='abrircanal')
    async def open_channel(self, ctx):
        if ctx.message.author.id != 193296310525231114:
            return

        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.message.delete()

        await ctx.send('Chat abrido', delete_after=2.0)


async def setup(bot):
    await bot.add_cog(Channels(bot))
