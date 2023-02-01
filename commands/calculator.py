from discord.ext import commands

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='soma')
    async def sum(self, ctx):
        response = str(ctx.message.content[14:])
        list_response = response.split(' ')
        try:
            list_response = [float(x) for x in list_response]
            sum_numbers = lambda soma : sum(soma)
            await ctx.send(sum_numbers(list_response))
        except ValueError:
            await ctx.send('Tem que ser só número')
    
    @commands.command(name='sub')
    async def sub(self, ctx):
        response = str(ctx.message.content[13:])
        list_response = response.split(' ')
        
        try:
            list_response = [float(x) for x in list_response]
            sub_numbers = list_response[0] - sum(list_response[1:])
            await ctx.send(sub_numbers)
        except ValueError:
            await ctx.send('Tem que ser só número')

    @commands.command(name='mult')
    async def mult(self, ctx):
        response = str(ctx.message.content[14:])
        list_response = response.split(' ')

        try:
            list_response = [float(x) for x in list_response]
            aux = list_response[0]
            for i in list_response[1:]:
                aux = aux * i
            await ctx.send(aux)
        except ValueError:
            await ctx.send('Tem que ser só número')
    
    @commands.command(name='div')
    async def div(self, ctx):
        response = str(ctx.message.content[13:])
        list_response = response.split(' ')
        
        try:
            list_response = [float(x) for x in list_response]
            div_numbers = lambda values : values[0]/values[1]
            await ctx.send(div_numbers(list_response))
        except ZeroDivisionError:
            await ctx.send('Vai dividir número por 0? kkkk sei nn em')
        except ValueError:
            await ctx.send('Tem que ser só número meu filho')

async def setup(bot):
    await bot.add_cog(Calculator(bot))