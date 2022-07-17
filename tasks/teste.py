from discord.ext import commands
from .bot_database import my_database

class Teste(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    database = my_database.My_Database

    con = database.connect()

    cursor = con.cursor()

    @commands.command(name='get_from_database')
    async def get(self, ctx):
        

        userid = self.database.get_user_database(447495979059642368, self.cursor)

        print(f'User id do teste: {userid}')
        print(type(userid))

        await ctx.send(userid)

def setup(bot):
    bot.add_cog(Teste(bot))