from discord.ext import commands
import asyncio

class Talks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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