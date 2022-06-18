from discord.ext import commands
import discord
import asyncio

class Jokenpo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='jokenpo')
    async def start_jokenpo(self, ctx, *members: discord.Member):
        members = list(members) #Get the users in a list
        members.append(ctx.author) #If the member who called the commands doesnt ping themself, it includes them
        first_member = members[0].id #Get the users ids
        second_member = members[1].id
        
        #Check if the next message sent is from one of the users mentioned in the command
        def check(msg):
            if msg.author.bot: 
                return
            return msg.author.id == first_member or msg.author.id == second_member

        #These two functions control the members playing the game
        def check_player_one(msg):
            if msg.author.bot:
                return
            return msg.author.id == first_member

        def check_player_two(msg):
            if msg.author.bot:
                return
            return msg.author.id == second_member
        
        await ctx.send('Jogo começando entre <@' + str(first_member) + '> e <@' + str(second_member) + '>')
        await asyncio.sleep(1)
        await ctx.send('Pedra, papel ou tesoura?')
        await asyncio.sleep(1)
        for i in range(3, 0, -1):
            await asyncio.sleep(1)
            await ctx.send(i)
        
        first_input = await self.bot.wait_for('message', check=check)
        try:
            if(first_input.author.id == first_member):
                second_input = await self.bot.wait_for('message', timeout=2.0, check=check_player_two)
            elif(first_input.author.id == second_member):
                second_input = await self.bot.wait_for('message', timeout=2.0, check=check_player_one)
        except asyncio.TimeoutError:
            await ctx.send('Demorou demais')

        #Save the ctx of the two players and delete the messages sent in chat by them
        first_user = first_input
        second_user = second_input

        await first_input.delete()
        await second_input.delete()

        await ctx.send(get_output_jokenpo(first_user, second_user))

def get_output_jokenpo(first_user, second_user):
    situation = [str(first_user.content).casefold(), str(second_user.content).casefold()]
    first_user_win = [['pedra', 'tesoura'], ['papel', 'pedra'], ['tesoura', 'papel']]
    second_user_win = [['tesoura', 'pedra'], ['pedra', 'papel'], ['papel', 'tesoura']]
    winner = ''

    if situation in first_user_win:
        winner = first_user.author.name
    elif situation in second_user_win:
        winner = second_user.author.name
    else:
        winner = 'Ninguém'

    return winner + ' ganhou'    

def setup(bot):
    bot.add_cog(Jokenpo(bot))