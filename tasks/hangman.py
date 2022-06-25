#Gotta rewrite this code...
#Gotta redo the logic, game changed
import random
import asyncio
from discord.ext import commands

class Hangman(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, msg):


    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.command(name='hangman')
    async def hangman_game(self, ctx):
        ctx_list = str(ctx.message.content).split(' ')
        word_to_be_guessed = ctx_list[2]
        characters_to_be_guessed = list(word_to_be_guessed)
        guessing_gaps = []
        users = []
        letters_guessed = []
        words_guessed = []

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
        a = 0
        while(a < len(characters_to_be_guessed)):
            msg = await msg.wait_for('message')
            if msg.content in characters_to_be_guessed







        """
        def check_turn(msg):
            return msg.author.id == player.id
        
        a = 0
        word_guessed = False
        while (a < len(word_to_be_guessed)) and not word_guessed:
            round_players = list.copy(users)
            await ctx.send('Seguimos...')
            await asyncio.sleep(1)
            await ctx.send('Começa uma nova rodada!')
            await asyncio.sleep(1)
            await ctx.send('Palavra: `' + ''.join(guessing_gaps) + '`')
            await asyncio.sleep(1)

            while round_players and not word_guessed:
                guessed_letter = None
                guessed_word = None
                player = random.choice(round_players)
                round_players.remove(player)
                await ctx.send('Jogador da vez: <@' + str(player.id) + '>')
                await asyncio.sleep(1)
                await ctx.send('Palavra ou letra?')
                choice = await self.bot.wait_for('message', check = check_turn)

                while (str(choice.content).casefold() != 'palavra') and (str(choice.content).casefold() != 'letra'):
                    await ctx.send('Não sabe ler não, paizão?')
                    await asyncio.sleep(1)
                    await ctx.send('Palavra ou letra?')
                    choice = await self.bot.wait_for('message', check = check_turn)

                if str(choice.content).casefold() == 'letra':
                    await ctx.send(str(player.name) + ', escolha uma letra!')
                    guessed_letter = await self.bot.wait_for('message', check = check_turn)
                    await ctx.send('A letra escolhida por ' + player.name + ' foi: ' + guessed_letter.content)
                    await asyncio.sleep(1)

                    while str(guessed_letter.content).casefold() in letters_guessed:
                        await ctx.send('Já tentaram essa, cabação!')
                        await asyncio.sleep(1)
                        await ctx.send(str(player.name) + ', escolhe outra!')
                        guessed_letter = await self.bot.wait_for('message', check = check_turn)
                        await ctx.send('A letra escolhida por ' + player.name + ' foi: ' + guessed_letter.content)

                    letters_guessed.append(str(guessed_letter.content).casefold())

                elif str(choice.content).casefold() == 'palavra':
                    await ctx.send(str(player.name) + ', dê o golpe de honra. Qual a palavra?')
                    guessed_word = await self.bot.wait_for('message', check = check_turn)
                    await ctx.send('A palavra escolhida por ' + player.name + ' foi: ' + guessed_word.content)
                    await asyncio.sleep(1)
                    
                    while str(guessed_word.content).casefold() in words_guessed:
                        await ctx.send('Presta atenção no grupo. Essa já tentaram.')
                        await asyncio.sleep(1)
                        await ctx.send(str(player.name) + ', tente o golpe de honra de novo!')
                        guessed_word = await self.bot.wait_for('message', check = check_turn)
                        await ctx.send('A palavra escolhida por ' + player.name + ' foi: ' + guessed_word.content)

                    words_guessed.append(str(guessed_word.content).casefold())

                if (guessed_letter is not None) and str(guessed_letter.content).casefold() in (char.casefold() for char in characters_to_be_guessed):
                    await ctx.send('Letra encontrada!')
                    await asyncio.sleep(1)            
                    for index, value in enumerate(word_to_be_guessed):
                        if str(guessed_letter.content).casefold() == value.casefold():
                            a += 1
                            index_aux = index * 2
                            guessing_gaps[index_aux] = guessed_letter.content
                            characters_to_be_guessed[index] = '0'
                            last_player = player

                elif (guessed_word is not None) and str(guessed_word.content).casefold() == word_to_be_guessed.casefold():
                    await ctx.send('Coé, acertou mesmo!')
                    await asyncio.sleep(1)
                    last_player = player
                    word_guessed = True
                else:
                    await ctx.send('BURRO! BURRO! BURRO! BURRO! BURRO! Tenta de novo na próxima rodada 💀')
                    await asyncio.sleep(1)

        await ctx.send('Rodada finalizada!')
        await asyncio.sleep(1)
        await ctx.send('A palavra era: ' + word_to_be_guessed)
        await asyncio.sleep(1)
        await ctx.send('Quem venceu a rodada: ' + last_player.mention)
        """

def setup(bot):
    bot.add_cog(Hangman(bot))