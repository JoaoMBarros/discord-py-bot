from discord.ext import commands
import random
import asyncio

class Bingo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bingo')
    async def bingo(self, ctx):
        starting_string = await ctx.send('Bingo começando')
        players = set()
        called_numbers = set()
        bingo_players = {}
        await starting_string.add_reaction('🍆')
        await asyncio.sleep(5)
        starting_string = await starting_string.channel.fetch_message(starting_string.id)

        #Getting players
        for reaction in starting_string.reactions:
            async for user in reaction.users():
                if user.id != self.bot.user.id:
                    players.add(user.id)
        
        #Creating and DM'ing each player their respective sequence of numbers
        for player in players:
            cartela_random = random.sample(range(0, 20), 5)
            bingo_players[player] = cartela_random
            aux = await self.bot.fetch_user(player)
            await aux.send(f'Sua cartela: {cartela_random}')
            
        def check(m):
            return m.content == 'BATI'

        possible_numbers = list(range(0, 50))

        while(True):

            await asyncio.sleep(2)
            await ctx.send('Próxima bola')
            await asyncio.sleep(2)
            aux = await ctx.send(random.choice(possible_numbers))

            possible_numbers.remove(int(aux.content))
            called_numbers.add(int(aux.content))

            try:
                winner = await self.bot.wait_for('message', check=check, timeout=5)

                await ctx.send('Bateu mesmo? Vou ver')

                await asyncio.sleep(5)

                value = bingo_players.get(winner.author.id)

                if all(x in called_numbers for x in value):
                    await ctx.send(f'<@{winner.author.id}> bateu. Aí é foda')
                    break
                else:
                    await ctx.send('Bateu o caralho')

            except asyncio.TimeoutError:
                pass

def setup(bot):
    bot.add_cog(Bingo(bot))