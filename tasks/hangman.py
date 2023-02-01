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

        def check_channel_and_host(m):
            if m.content == 'advpalavra parar' and m.author.id == ctx.message.author.id:
                return True
            return m.channel == ctx.message.channel and m.author.id == ctx.message.author.id
        
        def check_start(m):
            if m.content == 'advpalavra parar' and m.author.id == ctx.message.author.id:
                return True
            return m.content == 'advpalavra começar'

        food_string = await self.bot.wait_for('message', check=check_channel_and_host)

        if food_string.content == 'advpalavra parar':
            await ctx.send(embed=discord.Embed(title='Jogo finalizado', color=0xffffff))
            return

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
        
        start = await self.bot.wait_for('message', check=check_start)

        if start.content == 'advpalavra parar':
            await channel.send(embed=discord.Embed(title='Jogo finalizado', color=0xffffff))
            return
        
        embed = discord.Embed(title='**Um novo jogo está começando**', color=0x55acee)
        embed.set_author(name='Adivinhe a palavra!')
        embed.set_footer(text='Novo desafio em 10 segundos!')
        msg = await channel.send(embed=embed)

        rank_list = []
        rank = {}
        rounds = len(words_to_be_guessed)
        game_round = 0
        while words_to_be_guessed:
            game_round += 1
            def check(m):
                if m.content == 'advpalavra parar' and m.author.id == ctx.message.author.id:
                    return True
                return str(unidecode(m.content)).casefold() == str(unidecode(words_to_be_guessed[0])).casefold()

            async def check_40_seconds():
                try:
                    msg = await self.bot.wait_for('message', check=check, timeout=20)
                    return msg
                except asyncio.TimeoutError:
                    guessing_gaps[0] = characters_to_be_guessed[0]
                    embed = discord.Embed(title=f'🔍 **{str(hints[0])}**')
                    embed.set_author(name=f'Rodada {game_round}\n')
                    embed.add_field(name='\u200b', value='**Resposta:** `' + ''.join(guessing_gaps) + '`')
                    embed.set_footer(text='Faltam 40 segundos!', icon_url='https://media.giphy.com/media/waHLEK3f9iL2MKRy1t/giphy.gif')
                    await channel.send(embed=embed)
                    return False

            async def check_20_seconds():
                try:
                    msg = await self.bot.wait_for('message', check=check, timeout=20)
                    return msg
                except asyncio.TimeoutError:
                    guessing_gaps[-1] = characters_to_be_guessed[-1]
                    embed = discord.Embed(title=f'🔍 **{str(hints[0])}**')
                    embed.set_author(name=f'Rodada {game_round}\n')
                    embed.add_field(name='\u200b', value='**Resposta:** `' + ''.join(guessing_gaps) + '`')
                    embed.set_footer(text='Faltam 20 segundos!', icon_url='https://media.giphy.com/media/waHLEK3f9iL2MKRy1t/giphy.gif')
                    await channel.send(embed=embed)
                    return False

            guessing_gaps = []
            characters_to_be_guessed = list(words_to_be_guessed[0])
            for i in range(0, len(words_to_be_guessed[0]), 1):
                if characters_to_be_guessed[i] == ' ':
                    guessing_gaps.append(' ')
                else:
                    guessing_gaps.append('_')
                if i < len(words_to_be_guessed[0])-1:
                    guessing_gaps.append(' ')

            await asyncio.sleep(10)
            embed = discord.Embed(title=f'🔍 **{str(hints[0])}**')
            embed.set_author(name=f'Rodada {game_round}\n')
            embed.add_field(name='\u200b', value='**Resposta:** `' + ''.join(guessing_gaps) + '`')
            embed.set_footer(text='Faltam 60 segundos!', icon_url='https://media.giphy.com/media/waHLEK3f9iL2MKRy1t/giphy.gif')
            await channel.send(embed=embed)

            try:
                msg = await check_40_seconds()
                
                if not msg:
                    msg = await check_20_seconds()

                    if not msg:
                        msg = await self.bot.wait_for('message', check=check, timeout=20)

                if msg.content == 'advpalavra parar':
                    await channel.send(embed=discord.Embed(title='Jogo finalizado', color=0xffffff))
                    break

                user = await self.bot.fetch_user(msg.author.id)
                pfp = user.avatar
                pfp = pfp.with_size(128) if pfp != None else 'https://cdn.discordapp.com/attachments/658011360625688587/1069255545355239495/images152.jpg'  
                embed=discord.Embed(title=f'**{msg.author.name} acertou!**', description=f'A palavra era **{words_to_be_guessed[0]}**', color=0xc5ee55)
                embed.set_image(url=(pfp))
                embed.set_footer(text=f'Rodada {game_round} de {rounds}')
                await channel.send(embed=embed)

                if msg.author.id not in rank:
                    rank[msg.author.id] = 1
                else:
                    rank[msg.author.id] += 1
                
                words_to_be_guessed.pop(0)
                hints.pop(0)
                rank = dict(sorted(rank.items(), key=lambda item: item[1], reverse=True))
                rank_list = list(rank.items())

                await asyncio.sleep(5)
                medals = ['🥇', '🥈', '🥉']
                string_rank = ''
                for i in range(0, len(rank_list)):
                    if i > 2:
                        string_rank += f'🔹 <@{rank_list[i][0]}>**: {rank_list[i][1]}** pontos\n'
                    else:
                        string_rank += f'{medals[i]} <@{rank_list[i][0]}>**: {rank_list[i][1]}** pontos\n'
                    
                ranking=discord.Embed(title='**Classificação**', description=string_rank, color=0x55acee)
                ranking.set_author(name=f'Rodada {game_round}')
                ranking.set_footer(text='Nova rodada em 10 segundos')
                await channel.send(embed=ranking)

            except asyncio.TimeoutError:
                embed = discord.Embed(title='Acabou o tempo!', description=f'A palavra era **{words_to_be_guessed[0]}**', color=0xff4f4f)
                embed.set_image(url='https://i.imgur.com/uYc95q2.png')
                embed.set_footer(text=f'Rodada {game_round} de {rounds}')
                await channel.send(embed=embed)
                words_to_be_guessed.pop(0)
                hints.pop(0)

                await asyncio.sleep(5)
                medals = ['🥇', '🥈', '🥉']
                string_rank = ''
                for i in range(0, len(rank_list)):
                    if i > 2:
                        string_rank += f'🔹 <@{rank_list[i][0]}>**: {rank_list[i][1]}** pontos\n'
                    else:
                        string_rank += f'{medals[i]} <@{rank_list[i][0]}>**: {rank_list[i][1]}** pontos\n'
                    
                ranking=discord.Embed(title='**Classificação**', description=string_rank, color=0x55acee)
                ranking.set_author(name=f'Rodada {game_round}')
                ranking.set_footer(text='Nova rodada em 10 segundos')
                await channel.send(embed=ranking)
        
        rank = dict(sorted(rank.items(), key=lambda item: item[1], reverse=True))
        final_string = ''

        medals = ['🏆', '🥈', '🥉']
        places = ['Maior pontuador:', 'Segundo lugar:', 'Terceiro lugar:']

        for i in range(0, len(rank_list)):
            if i > 2:
                break
            final_string += f'{medals[i]} **{places[i]}** <@{rank_list[i][0]}> (**{rank_list[i][1]}** pontos)\n'

        ranking=discord.Embed(title='**Classificação final**\n\n', description=final_string, color=0xffcc4d)
        ranking.set_author(name='Fim de jogo!')
        ranking.set_footer(text='Obrigado por participar!', icon_url='https://i.imgur.com/zJ8dnY6.png')

        await asyncio.sleep(5)
        await channel.send(embed=ranking)

async def setup(bot):
    await bot.add_cog(Hangman(bot))