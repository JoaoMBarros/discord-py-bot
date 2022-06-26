# Mudar o sistema de react
# Arrumar o bot pra só quem iniciou o comando conseguir usar os comandos de controle
# Bot reagir a uma mensagem quando ela se aproximar da resposta correta

import asyncio
from unidecode import unidecode
from discord.ext import commands
import discord

class Hangman(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
    @commands.command(name='advpalavra')
    async def hangman_game(self, ctx):
        channel = self.bot.get_channel(716290570833887262)
        await ctx.send('Alimente o bot')

        def check_channel(m):
            return m.channel == ctx.message.channel
        
        def check_start(m):
            if m.content == 'advpalavra parar':
                return True
            return m.content == 'advpalavra começar'

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

        if start.content == 'advpalavra parar':
            await channel.send('Jogo parado')
            return
        
        embed = discord.Embed(title='**Jogo começando!**', color=0x89CFF0)
        embed.add_field(name='\u200b', value='🔥 Reaja para participar')

        msg = await channel.send(embed=embed)
        await msg.add_reaction('🔥')
        await asyncio.sleep(30)
        msg = await channel.fetch_message(msg.id)

        for reaction in msg.reactions:
            async for user in reaction.users():
                if user != self.bot.user:
                    users.append(user)
        
        rank = {}
        for key in users:
            rank[key.id] = 0
        
        while words_to_be_guessed:

            string_rank = ''
            rank = dict(sorted(rank.items(), key=lambda item: item[1], reverse=True))
            for player, score in rank.items():
                string_rank += '**{}**: {}'.format('<@'+str(player)+'>', str(score)+' pontos\n')
            
            ranking=discord.Embed(title='**RANKING**', color=0xb9e85a)
            ranking.add_field(name='\u200b', value=string_rank)
            await channel.send(embed=ranking)

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
            embed = discord.Embed(title='**Dica: ' + str(hints[0]) + '**')
            embed.add_field(name='\u200b', value='Palavra: `' + ''.join(guessing_gaps) + '`')
            await channel.send(embed=embed)

            def check(m):
                if m.content == 'advpalavra parar' and m.author.id in users.id:
                    return True
                return str(unidecode(m.content)).casefold() == str(unidecode(words_to_be_guessed[0])).casefold() and m.author.id in [x.id for x in users]

            async def check_40_seconds():
                channel = self.bot.get_channel(716290570833887262)
                try:
                    msg = await self.bot.wait_for('message', check=check, timeout=20)
                    return msg
                except asyncio.TimeoutError:
                    guessing_gaps[0] = characters_to_be_guessed[0]
                    embed = discord.Embed(title='**Dica: ' + str(hints[0]) + '**', description='Faltam 40 segundos!')
                    embed.add_field(name='\u200b', value='Palavra: `' + ''.join(guessing_gaps) + '`')
                    await channel.send(embed=embed)
                    return False

            async def check_20_seconds():
                channel = self.bot.get_channel(716290570833887262)
                try:
                    msg = await self.bot.wait_for('message', check=check, timeout=20)
                    return msg
                except asyncio.TimeoutError:
                    guessing_gaps[-1] = characters_to_be_guessed[-1]
                    embed = discord.Embed(title='**Dica: ' + str(hints[0]) + '**', description='Faltam 20 segundos!')
                    embed.add_field(name='\u200b', value='Palavra: `' + ''.join(guessing_gaps) + '`')
                    await channel.send(embed=embed)
                    return False

            try:
                msg = await check_40_seconds()
                
                if not msg:
                    msg = await check_20_seconds()

                    if not msg:
                        msg = await self.bot.wait_for('message', check=check, timeout=20)

                if msg.content == 'advpalavra parar':
                    break
                
                user = await self.bot.fetch_user(msg.author.id)
                pfp = user.avatar_url_as(size=128)
        
                embed=discord.Embed(title='**' + msg.author.name+' acertou!**', description="Palavra: **"+words_to_be_guessed[0] + '**', color=0xb9e85a)
                embed.set_image(url=(pfp))

                await channel.send(embed=embed)

                rank[msg.author.id] += 1
                words_to_be_guessed.pop(0)
                hints.pop(0)
                await asyncio.sleep(3)

            except asyncio.TimeoutError:
                
                embed = discord.Embed(title='Acabou o tempo!', description='Ninguém acertou', color=0xff4f4f)
                embed.add_field(name='\u200b', value='A palavra era: **`' + ''.join(characters_to_be_guessed) + '`**')
                await channel.send(embed=embed)


                words_to_be_guessed.pop(0)
                hints.pop(0)
                await asyncio.sleep(3)
        
        rank = dict(sorted(rank.items(), key=lambda item: item[1], reverse=True))
        await asyncio.sleep(3)

        podium = []
        for i in range(0, len(rank.items())):
            podium.append([str(list(rank)[i]), str(list(rank.values())[i])])
            if i > 2:
                break
        
        final_string = ''

        if len(podium) == 1:
            final_string += '🏆 **Maior pontuador:** ' + '<@' + ''.join(str(podium[0][0])) + '> (' + ''.join(str(podium[0][1]) + ' pontos)')
        elif len(podium) == 2:
            final_string += '🏆 **Maior pontuador:** ' + '<@' + ''.join(str(podium[0][0])) + '> (' + ''.join(str(podium[0][1]) + ' pontos)\n')
            final_string += '🥈 **Segundo lugar:** ' + '<@' + ''.join(str(podium[1][0])) + '> (' + ''.join(str(podium[1][1]) + ' pontos)')
        elif len(podium) == 3:
            final_string += '🏆 **Maior pontuador:** ' + '<@' + ''.join(str(podium[0][0])) + '> (' + ''.join(str(podium[0][1]) + ' pontos)\n')
            final_string += '🥈 **Segundo lugar:** ' + '<@' + ''.join(str(podium[1][0])) + '> (' + ''.join(str(podium[1][1]) + ' pontos)\n')
            final_string += '🥉 **Terceiro lugar:** ' + '<@' + ''.join(str(podium[2][0])) + '> (' + ''.join(str(podium[2][1]) + ' pontos)')

        ranking=discord.Embed(title='**FIM DE JOGO!**\n\n', color=0xb9e85a)
            
        ranking.add_field(name='\u200b', value=final_string)

        await channel.send(embed=ranking)

def setup(bot):
    bot.add_cog(Hangman(bot))