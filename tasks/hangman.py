# Colocar um sistema de reaction para participar
# Escolher randomicamente qual o jogador da vez
# Colocar um sistema para poderem tentar descobrir a palavra de uma vez
# Uma mensagem de finalização no final

import asyncio
from discord.ext import commands

class Hangman(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='hangman')
    async def hangman_game(self, ctx):
        word_to_be_guessed = 'Merengue'
        characters_to_be_guessed = list(word_to_be_guessed)
        guessing_gaps = []

        for i in range(0, len(word_to_be_guessed), 1):
            print(i)
            guessing_gaps.append('_')
            if i < len(word_to_be_guessed)-1:
                guessing_gaps.append(' ')
        
        await ctx.send('Palavra: `' + ''.join(guessing_gaps) + '`')
        
        def check(msg):
            return ctx.author == msg.author
    
        a = 0
        while a < len(word_to_be_guessed):
            await ctx.send('<@447495979059642368>, escolha uma letra!')
            guessed_letter = await self.bot.wait_for('message', check = check)
            await ctx.send('A letra escolhida por :mention: foi: ' + guessed_letter.content)
            await asyncio.sleep(2)
            await ctx.send('Temos essa letra?')
            await asyncio.sleep(2)

            if guessed_letter.content in characters_to_be_guessed:            
                for index, value in enumerate(word_to_be_guessed):
                    if guessed_letter.content == value:
                        a += 1
                        index_aux = index * 2
                        guessing_gaps[index_aux] = guessed_letter.content
                        characters_to_be_guessed[index] = '0'
                        await ctx.send('Letra encontrada! `' + ''.join(guessing_gaps) + '`')
                        await asyncio.sleep(2)
            else:
                await ctx.send('BURRO! Letra não encontrada 💀')
                await asyncio.sleep(2)

        await ctx.send('Palavra finalizada!\nA palavra era: ' + word_to_be_guessed)



def setup(bot):
    bot.add_cog(Hangman(bot))
