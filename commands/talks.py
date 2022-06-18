import random
import requests
from translate import Translator
from discord.ext import commands

class Talks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """@commands.Cog.listener()
    async def on_message(self, message):
        ctx = await self.bot.get_context(message)
        if message.author == self.bot.user:
            return
        else:
            message_count += 1

        if message_count == 50:
            await self.send_message_sabio(ctx)"""
  
    @commands.command(name='sabio')
    async def send_message_sabio(self, ctx):
        translator = Translator(to_lang='pt')
        response = requests.get('https://api.adviceslip.com/advice')
        advice_json = response.json()
        advice = advice_json['slip']['advice']
        await ctx.message.delete()
        await ctx.send(translator.translate(advice))
    
    @commands.command(name='maconha')
    async def send_message_maconha(self, ctx):
        roulette = ['<@987100450954285097>', '<@383320582336413706>']
        response = random.choice(roulette)
        await ctx.send(response)

    @commands.command(name='roteiro')
    async def send_message_roteiro(self, ctx):
        response = 'O roteiro está ' + str(random.randint(0, 99)) + '% pronto'
        await ctx.send(response)

    @commands.command(name='cap')
    async def send_message_cap(self, ctx):
        response = """Não se preocupe que em breve sairão alguns capítulos. Parte da equipe está bem atarefada ou com outros projetos ou com problemas pessoais/escola/universidade/trabalho, aí o processo é mais lento do que já era.
Se não quiser ler em inglês, tem um pessoal no facebook que fazia a tradução deles, e até onde eu lembro, era bem rápida. Não faço ideia de onde eles pegam a tradução ou da qualidade deles, mas deve ajudar se o seu inglês não for afiado. Aí você decide se quer revisitar o nosso mais tarde ou não
Mas não se preocupe que não paramos de fazer não, só estamos mais ocupados e não queremos cortar a qualidade por conta disso. Espero que entenda"""
        await ctx.message.delete()
        await ctx.send(response)

    @commands.command(name='hg')
    async def send_message_hg(self, ctx):
        response = 'Hg só quando o Grêmio ganhar'
        await ctx.message.delete()
        await ctx.send(response)

def setup(bot):
    bot.add_cog(Talks(bot))