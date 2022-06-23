from discord.ext import commands

class Mangas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='info')
    async def get_info_manga(self, ctx):
        f = open('mangas.txt', 'r', encoding = 'utf-8')
        manga_name = str(ctx.message.content)[14:]
        string_info = ''
        for line in f:
            if (line == 'Mangá: ' + manga_name):
                string_info += line
                
        await ctx.send(f.read())

def setup(bot):
    bot.add_cog(Mangas(bot))