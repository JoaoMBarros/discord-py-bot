from discord.ext import commands
import asyncio
class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #This function needs a full rewrite. Way too polluted
    @commands.command(name='votacao', description='Faz uma votacao kk')
    async def start_poll(self, ctx):

        #Breaking the string command and creating a list with all substrings
        string_list = str(ctx.message.content)[17:]
        string_list = string_list.split('^')

        #Getting the timer
        time = int(string_list.pop(0))

        poll_options = []
        choosen_emotes = []
        poll_string = ''

        #Grabbing the emotes and the poll options sent with the command
        while string_list:
            choosen_emotes.append(string_list.pop(0))
            poll_options.append(string_list.pop(0))
        
        #Striping the space characters from the elements of the emotes list
        choosen_emotes = [s.strip(' ') for s in choosen_emotes]

        #Creating the poll string        
        for i in range(0, len(poll_options), 1):
            poll_string += str(choosen_emotes[i]) + ' ➜ ' + str(poll_options[i]) + '\n'

        poll_string = await ctx.send(poll_string)

        winners = []
        poll_emotes_count = []
        
        #Adding the reactions to it
        for emote in choosen_emotes:
            await poll_string.add_reaction(emote)
        
        #Time until the poll ends
        await asyncio.sleep(time)
    
        #Getting the quantity of each reaction
        poll_string = await poll_string.channel.fetch_message(poll_string.id)
        for reaction in poll_string.reactions:
            poll_emotes_count.append(reaction.count)

        #Getting the winner(s)
        aux = -1
        for i in poll_string.reactions:
            aux += 1
            if i.count == max(poll_emotes_count):
                winner_emote = choosen_emotes[aux]
                winners.append(poll_options[aux])

        winners = [s.strip(' ') for s in winners]
        winner_message = 'Empate entre **'

        if len(winners) == 1:
            winner_message = str(winner_emote) + ' ' + winners[0] + ' venceu.'
        elif len(winners) == 2:
            winner_message += str(winners[0]) + '** e **' + str(winners[1]) + '**.'
        else:
            for i in range(0, len(winners)):
                if i < len(winners)-1:
                    winner_message += winners[i] + '**, **'
                else:
                    winner_message = winner_message[:-6]
                    winner_message += '** e **' + winners[-1] + '**.'
        await ctx.send(winner_message)
        
    @commands.command(name="pingcana")
    async def send_ping_cana(self, ctx):
        msg = await ctx.channel.send('Eu devo pingar o cana?')
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        await asyncio.sleep(15)
        msg = await msg.channel.fetch_message(msg.id)
        positive = 0
        negative = 0
        for reaction in msg.reactions:
            if reaction.emoji == '👍':
                positive = reaction.count - 1
            if reaction.emoji == '👎':
                negative = reaction.count - 1
        
        if positive > negative:
            await ctx.channel.send("<@383320582336413706>")
        else:
            await ctx.channel.send("Não foi dessa vez")   


def setup(bot):
    bot.add_cog(Reactions(bot))