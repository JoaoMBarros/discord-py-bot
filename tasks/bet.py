from discord.ext import commands
import asyncio

class Bet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='aposta')
    async def start_poll(self, ctx):

        #Breaking the string command and creating a list with all substrings
        string_list = str(ctx.message.content)[16:]
        string_list = string_list.split('^')

        await ctx.message.delete()

        #Getting the timer
        time = int(string_list.pop(0))

        poll_options = []
        choosen_emotes = []
        poll_string = ''

        #Grabbing the emotes and the poll options sent with the command
        while string_list:
            choosen_emotes.append(string_list.pop(0))
            poll_options.append(string_list.pop(0))
        
        #Creating the poll string        
        for i in range(0, len(poll_options), 1):
            poll_string += str(choosen_emotes[i]) + ' ➜ ' + str(poll_options[i]) + '\n'

        poll_string = await ctx.send(poll_string)

        winners = []
        poll_emotes_count = []
        
        poll_string.add_reaction('✅')
        
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
        
def setup(bot):
    bot.add_cog(Bet(bot))