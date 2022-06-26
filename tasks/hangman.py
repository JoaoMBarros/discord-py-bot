#Gotta rewrite this code...
#Gotta redo the logic, game changed
import asyncio
from unidecode import unidecode
from discord.ext import commands

class Hangman(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.command(name='hangman')
    async def hangman_game(self, ctx):
        channel = self.bot.get_channel(716000401618370660)
        await ctx.send('Alimente o bot')

        def check_channel(m):
            return m.channel == ctx.message.channel
        
        def check_start(m):
            if m.content == 'hangman parar':
                return True
            return m.content == 'hangman começar'

        food_string = await self.bot.wait_for('message', check=check_channel)
        await ctx.send('Bot alimentado')

        food_list = str(food_string.content).split('^')
        aux_strip_items = []
        for element in food_list:
            aux_strip_items.append(element.strip())

        new_food_list = []
        for element in aux_strip_items:
            new_food_list.append(element.split('\n'))
    
        word_hint_dict = dict(new_food_list)
        words_to_be_guessed = list(word_hint_dict.keys())
        hints = list(word_hint_dict.values())
        users = []
        
        start = await self.bot.wait_for('message', check=check_start)

        if start.content == 'hangman parar':
            await ctx.send('Jogo parado')
            return
        
        msg = await channel.send('Começando o jogo. React pra participar')
        await msg.add_reaction('🔥')
        await asyncio.sleep(5)
        msg = await channel.fetch_message(msg.id)

        for reaction in msg.reactions:
            async for user in reaction.users():
                if user != self.bot.user:
                    users.append(user)
        
        rank = {}

        for key in users:
            rank[key.name] = 0
        
        while words_to_be_guessed:

            for player, score in rank.items():
                string_rank = '**RANKING DA PARTIDA:**\n\n**{}**: {}'.format(player, score)
            
            await ctx.send(string_rank)

            guessing_gaps = []
            characters_to_be_guessed = list(words_to_be_guessed[0])

            for i in range(0, len(words_to_be_guessed[0]), 1):
                if characters_to_be_guessed[i] == ' ':
                    guessing_gaps.append(' ')
                else:
                    guessing_gaps.append('_')
                if i < len(words_to_be_guessed[0])-1:
                    guessing_gaps.append(' ')

            await asyncio.sleep(5)
            await channel.send('A dica é: ' + hints[0] + '\nPalavra: `' + ''.join(guessing_gaps) + '`')

            def check(m):
                if m.content == 'hangman parar':
                    return True
                return str(unidecode(m.content)).casefold() == str(unidecode(words_to_be_guessed[0])).casefold()
            
            async def check_50_seconds():
                channel = self.bot.get_channel(716000401618370660)
                try:
                    msg = await self.bot.wait_for('message', check=check, timeout=10)
                    return msg
                except asyncio.TimeoutError:
                    guessing_gaps[0] = characters_to_be_guessed[0]
                    await channel.send('A dica é: ' + hints[0] + '\nPalavra: `' + ''.join(guessing_gaps) + '`')
                    return False

            async def check_30_seconds():
                channel = self.bot.get_channel(716000401618370660)
                try:
                    msg = await self.bot.wait_for('message', check=check, timeout=20)
                    return msg
                except asyncio.TimeoutError:
                    guessing_gaps[-1] = characters_to_be_guessed[-1]
                    await channel.send('A dica é: ' + hints[0] + '\nPalavra: `' + ''.join(guessing_gaps) + '`')
                    return False
            
            async def check_10_seconds():
                channel = self.bot.get_channel(716000401618370660)
                try:
                    msg = await self.bot.wait_for('message', check=check, timeout=10)
                    return msg
                except asyncio.TimeoutError:
                    await channel.send('Faltam 10 segundos')
                    return False

            try:
                msg = await check_50_seconds()
                
                if not msg:
                    msg = await check_30_seconds()
                
                    if not msg:
                        msg = await check_10_seconds()

                        if not msg:
                            msg = await self.bot.wait_for('message', check=check, timeout=10)

                if msg.content == 'hangman parar':
                    break

                await channel.send('Acertou')
                rank[msg.author.name] += 1
                words_to_be_guessed.pop(0)
                hints.pop(0)
                asyncio.sleep(3)
            except asyncio.TimeoutError:
                words_to_be_guessed.pop(0)
                hints.pop(0)
                await channel.send('Acabou o tempo!\nA palavra era ' + ''.join(characters_to_be_guessed))
                asyncio.sleep(3)
        
        await ctx.send('Fim de jogo')

        for player, score in rank.items():
                string_rank = '**{}**: {}'.format(player, score)

        string_final = '**RANKING FINAL**\n\n' + string_rank

        await ctx.send(string_final)

def setup(bot):
    bot.add_cog(Hangman(bot))