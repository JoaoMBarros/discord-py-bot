from discord.ext import commands
from bot_database import my_database

class Teste(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    database = my_database.My_Database

    con = database.connect()

    cursor = con.cursor()

    @commands.command(name='get_from_database')
    async def get(self, ctx):
        
        print(self.con.is_connected())
        
        userid = self.database.get_user(self.con, self.cursor, ctx.message.author.id)
        coins_user = self.database.get_user_coins(self.cursor, ctx.message.author.id)
        victories = self.database.get_user_bingo_victories(self.cursor, ctx.message.author.id)

        
        await ctx.send(f'Teu id {userid}')
        await ctx.send(f'Teus coins {coins_user}')
        await ctx.send(f'Tuas vitorias {victories}')
        

def setup(bot):
    bot.add_cog(Teste(bot))