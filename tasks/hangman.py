#O "nao sabe ler nao, paizao?" nao ta loopando

import random
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
        users = []

        msg = await ctx.send('Começando o jogo. React pra participar')
        await msg.add_reaction('🔥')
        await asyncio.sleep(5)
        msg = await ctx.channel.fetch_message(msg.id)

        for reaction in msg.reactions:
            async for user in reaction.users():
                if user != self.bot.user:
                    users.append(user)

        for i in range(0, len(word_to_be_guessed), 1):
            guessing_gaps.append('_')
            if i < len(word_to_be_guessed)-1:
                guessing_gaps.append(' ')

        def check_turn(msg):
            return msg.author.id == player.id

        word_guessed = False
        a = 0
        while (a < len(word_to_be_guessed)) and not word_guessed:
            round_players = list.copy(users)
            await ctx.send('Seguimos...')
            await asyncio.sleep(2)
            await ctx.send('Começa uma nova rodada!')
            await asyncio.sleep(2)
            await ctx.send('Palavra: `' + ''.join(guessing_gaps) + '`')
            await asyncio.sleep(1)

            while round_players and not word_guessed:
                guessed_letter = None
                guessed_word = None
                player = random.choice(round_players)
                round_players.remove(player)
                await ctx.send('Jogador da vez: <@' + str(player.id) + '>')
                await asyncio.sleep(2)
                await ctx.send('Palavra ou letra?')
                choice = await self.bot.wait_for('message', check = check_turn)

                if str(choice.content).casefold() == 'letra':
                    await ctx.send(str(player.name) + ', escolha uma letra!')
                    guessed_letter = await self.bot.wait_for('message', check = check_turn)
                    await ctx.send('A letra escolhida por :mention: foi: ' + guessed_letter.content)
                    await asyncio.sleep(2)
                    await ctx.send('Temos essa letra?')
                    await asyncio.sleep(2)

                elif str(choice.content).casefold() == 'palavra':
                    await ctx.send(str(player.name) + ', dê o golpe de honra. Qual a palavra?')
                    guessed_word = await self.bot.wait_for('message', check = check_turn)
                    await ctx.send('A palavra escolhida por :mention: foi: ' + guessed_word.content)

                else:
                    await ctx.send('Não sabe ler não, paizão?')
                    await asyncio.sleep(1)
                    await ctx.send('Palavra ou letra?')
                    choice = await self.bot.wait_for('message', check = check_turn)

                if (guessed_letter is not None) and guessed_letter.content in characters_to_be_guessed:            
                    for index, value in enumerate(word_to_be_guessed):
                        if guessed_letter.content == value:
                            a += 1
                            index_aux = index * 2
                            guessing_gaps[index_aux] = guessed_letter.content
                            characters_to_be_guessed[index] = '0'
                            await ctx.send('Letra encontrada! `' + ''.join(guessing_gaps) + '`')
                            await asyncio.sleep(2)
                            last_player = player

                elif (guessed_word is not None) and guessed_word.content == word_to_be_guessed:
                    await ctx.send('Coé, acertou mesmo!')
                    await asyncio.sleep(2)
                    last_player = player
                    word_guessed = True
                else:
                    await ctx.send('BURRO! BURRO! BURRO! BURRO! BURRO! Tenta de novo na próxima rodada 💀')
                    await asyncio.sleep(2)
                
        await ctx.send('Palavra finalizada!\nA palavra era: ' + word_to_be_guessed)
        await ctx.send('Quem venceu a rodada: ' + last_player.mention)

def setup(bot):
    bot.add_cog(Hangman(bot))
