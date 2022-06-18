from discord.ext import commands
import discord

class Jokenpo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='jokenpo')
    async def start_jokenpo(self, ctx, *members: discord.Member):
        members = list(members)
        members.append(ctx.author)
        await ctx.send('Pedra, papel ou tesoura?')
        
        def check(msg):
            if msg.author.bot:
                return
            else:
                return msg

        await ctx.send('Em')
        for i in range(3, 0, -1):
            await ctx.send(i)
            
        first_input = await self.bot.wait_for('message')
        second_input = await self.bot.wait_for('message')
        first_user = first_input
        second_user = second_input

        await first_input.delete()
        await second_input.delete()

        await ctx.send(get_output_jokenpo(first_user, second_user))

def get_output_jokenpo(first_user, second_user):
    winner = ''
    match first_user.content:
        case 'pedra':
            if (second_user.content == 'papel'):
                winner = second_user.author.name
            elif(second_user.content == 'tesoura'):
                winner = first_user.author.name
            elif(second_user.content == 'pedra'):
                winner = 'Ninguém'
        case 'papel':
            if (second_user.content == 'papel'):
                winner = 'Ninguém'
            elif(second_user.content == 'pedra'):
                winner = first_user.author.name
            elif(second_user.content == 'tesoura'):
                winner = second_user.author.name
        case 'tesoura':
            if (second_user.content == 'papel'):
                winner = first_user.author.name
            elif(second_user.content == 'tesoura'):
                winner = 'Ninguém'
            elif(second_user.content == 'pedra'):
                winner = second_user.author.name

    return winner + ' ganhou'    

def setup(bot):
    bot.add_cog(Jokenpo(bot))