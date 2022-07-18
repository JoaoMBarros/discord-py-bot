from discord.ext import commands
import random
import asyncio
import discord
import time
import mysql.connector

class Bingo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bingo')
    async def bingo(self, ctx):
        database = connection()
        cursor = database.cursor()
        if not database:
            print('Falha na conexao com o banco de dados')
            exit(1)
            
        starting_game_embed = discord.Embed(title='Um novo jogo está começando', color=0x55ACEE)
        starting_game_embed.set_footer(text='Reaja com ✋ para participar e receber sua cartela')
        starting_game_embed.set_author(name='Bingo da Senryuu')

        starting_string = await ctx.send(embed=starting_game_embed)
        players = set()
        called_numbers = set()
        bingo_players = {}
        await starting_string.add_reaction('✋')
        await asyncio.sleep(5)
        starting_string = await starting_string.channel.fetch_message(starting_string.id)

        #Getting players
        for reaction in starting_string.reactions:
            async for user in reaction.users():
                if user.id != self.bot.user.id:
                    players.add(user.id)
        
        #Creating and DM'ing each player their respective sequence of numbers
        for player in players:
            cartela_random = random.sample(range(1, 5), 1)
            bingo_players[player] = cartela_random
            aux = await self.bot.fetch_user(player)
            await aux.send(f'Sua cartela: {cartela_random}')
            
        def check(m):
            return str(m.content).casefold() == 'bati'

        possible_numbers = list(range(1, 6))


        start_time = time.time()
        while(True):
            
            aux = await ctx.send(embed=discord.Embed(title='Rolando...', color=0x00FFFF))
            await asyncio.sleep(3)
            await aux.delete()

            aux = random.choice(possible_numbers)
            possible_numbers.remove(aux)
            called_numbers.add(aux)
            
            cursor.execute(f'SELECT bingo_image_link FROM bingo_images WHERE id_image = {aux}')
            get_image_link_from_db = cursor.fetchone()

            
            await ctx.send(get_image_link_from_db[0])
            await ctx.send(embed=discord.Embed( title='Bolas sorteadas', 
                                                description=' - '.join(f'{k}' for k in called_numbers), 
                                                color=0x00FFFF) )

           
            try:
                winner = await self.bot.wait_for('message', check=check, timeout=5)

                await ctx.send(embed=discord.Embed(title='Bateu é?', color=0x00FFFF), reference=winner, mention_author=False)

                await asyncio.sleep(5)

                value = bingo_players.get(winner.author.id)

                if all(x in called_numbers for x in value):
                    finish_time = time.time()
                    await ctx.send(embed=discord.Embed(title=f'<@{winner.author.id}> bateu. Aí é foda', color=0x00FFFF))
                    await ctx.send(finish_time)
                    await ctx.send(f'start_time {finish_time-start_time}')
                    break
                else:
                    await ctx.send(embed=discord.Embed(title='Só se foi a cabeça 😂😂😂', color=0x00FFFF))
                    await asyncio.sleep(3)

            except asyncio.TimeoutError:
                pass

def connection():
    con = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net', database='heroku_14d4793a8dd9a42', user='bc3c162b414dfa', password='ff17f6c2')
    if con.is_connected():
        return con
    else:
        return False

def close_connection(con, cursor):
    cursor.close()
    con.close()

def setup(bot):
    bot.add_cog(Bingo(bot))