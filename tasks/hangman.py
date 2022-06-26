#Gotta rewrite this code...
#Gotta redo the logic, game changed
import asyncio
from discord.ext import commands

class Hangman(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.command(name='hangman')
    async def hangman_game(self, ctx):
        await ctx.send('Alimente o bot')

        def check_channel(m):
            return m.channel == ctx.message.channel

        food_string = await self.bot.wait_for('message', check=check_channel)
        food_list = str(food_string.content).split('^')

        aux_strip_items = []
        for element in food_list:
            aux_strip_items.append(element.strip())

        new_food_list = []
        for element in aux_strip_items:
            new_food_list.append(element.split('\n'))
    
        word_hint_dict = dict(new_food_list)
        words_to_be_guessed = list(word_hint_dict.keys())

        while words_to_be_guessed:
        
            characters_to_be_guessed = list(words_to_be_guessed[0])
            guessing_gaps = []
            users = []

            msg = await ctx.send('Começando o jogo. React pra participar')
            await msg.add_reaction('🔥')
            await asyncio.sleep(5)
            msg = await ctx.channel.fetch_message(msg.id)

            for reaction in msg.reactions:
                async for user in reaction.users():
                    if user != self.bot.user:
                        users.append(user)
            
            for i in range(0, len(words_to_be_guessed[0]), 1):
                if characters_to_be_guessed[i] == ' ':
                    guessing_gaps.append(' ')
                else:
                    guessing_gaps.append('_')
                if i < len(words_to_be_guessed[0])-1:
                    guessing_gaps.append(' ')

            await ctx.send('Palavra: `' + ''.join(guessing_gaps) + '`')
            
            

            def check(m):
                if str(m.content).casefold() == 'hangman stop':
                    exit(1)
                return str(m.content).casefold() == words_to_be_guessed[0].casefold()
            
            async def check_50_seconds():
                channel = self.bot.get_channel(716000401618370660)
                try:
                    await self.bot.wait_for('message', check=check, timeout=10)
                    return True
                except asyncio.TimeoutError:
                    await channel.send('Primeira dica! A palavra começa com ' + characters_to_be_guessed[0])
                    guessing_gaps[0] = characters_to_be_guessed[0]
                    await ctx.send('Palavra: `' + ''.join(guessing_gaps) + '`')
                    await channel.send('Faltam 50 segundos!\n')
                    return False

            async def check_30_seconds():
                channel = self.bot.get_channel(716000401618370660)
                try:
                    await self.bot.wait_for('message', check=check, timeout=20)
                    return True
                except asyncio.TimeoutError:
                    await channel.send('Segunda dica! A palavra termina com ' + characters_to_be_guessed[-1])
                    guessing_gaps[-1] = characters_to_be_guessed[-1]
                    await ctx.send('Palavra: `' + ''.join(guessing_gaps) + '`')
                    await channel.send('Faltam 30 segundos')
                    return False
            
            async def check_10_seconds():
                channel = self.bot.get_channel(716000401618370660)
                try:
                    await self.bot.wait_for('message', check=check, timeout=10)
                    return True
                except asyncio.TimeoutError:
                    await channel.send('Faltam 10 segundos')
                    return False

            try:
                return_value_50 = await check_50_seconds()
                
                if not return_value_50:
                    return_value_30 = await check_30_seconds()
                
                    if not return_value_30:
                        return_value_10 = await check_10_seconds()

                        if not return_value_10:
                            msg = await self.bot.wait_for('message', check=check, timeout=10)

                await ctx.send('Acertou')
                words_to_be_guessed.pop(0)
            except asyncio.TimeoutError:
                await ctx.send(characters_to_be_guessed)
                await ctx.send('Acabou o tempo')

def setup(bot):
    bot.add_cog(Hangman(bot))