from discord.ext import commands
import random

class Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bolso')
    async def send_message_roteiro(self, ctx):
        response = ['termina o video', 'abre o app', 'faz o video', 'faz flexão militar', 
                    'cria o servidor', 'abre o jogo', 'vai bed', 'faz o qc', 'faz o evento', 
                    'faz o gartic', 'faz o hg', 'faz o cap', 'faz o drink', 'manda o audio', 
                    'ganha o mundial', 'entra no autocar', 'diminui o dolar', 'assiste bojack', 
                    'assiste baby steps', 'assiste ousama game', 'assiste ousama ranking', 
                    'assiste euphoria', 'faz o roteiro', 'abre o mine', 'joga hollow knight', 
                    'le classroom', 'assiste link click', 'paga academia', 'cade a namorada', 
                    'loga no fortnite', 'acha o jogo', 'le ohayou ibarahime', 'assiste rwby']

        await ctx.send(random.choice(response))

    @commands.command(name='lucy')
    async def send_message_lucy(self, ctx):
        response = 'Shirogane abalava os arredores da escola com o rebolar de sua bunda. Todos não conseguiam parar de olhar aquela vista divina, que subia e descia junto com ele, naquele pole dance que foi instalado no salão principal, especialmente para ele.' \
        ' No começo ele não era muito bom em dançar naquilo, mas com o passar do tempo foi se tornando um profissional do ramo. Kaguya gostava dele, mas acabou tendo seu amor roubado por Ishigami, que teve a iniciativa de falar que gostaria de dar para Shirogane, e ela não tinha iniciativa nenhuma, sempre se prendendo a uma vergonha sem sentido.\n\n' \
        'Atualmente, Ishigami e Shirogane estão casados e com três filhos. Ishigami aceitou, depois de muitas reclamações, que Shirogane continuasse com seu trabalho de prostituto, afinal, aquela era a única forma de renda que ele tinha, e não gostaria de perder só porque o amor da vida dele não gostava de traição.'
        await ctx.message.delete()
        await ctx.send(response)

    @commands.command(name='trap')
    async def send_message_trap(self, ctx):
        response = 'o trap já engoliu muita porra calado, já tomou muito no rabo, já fuderam ele varias vezes, já aguentou cada cacete na vida, muita bolada nas costas, muita paulada por trás, já machucaram muito por dentro, já meteram muito o pau nele'
        await ctx.message.delete()
        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(Members(bot))