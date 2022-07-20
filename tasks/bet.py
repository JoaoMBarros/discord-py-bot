from discord.ext import commands
import asyncio

class Bet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='aposta')
    async def start_poll(self, ctx):

        #Breaking the string command and creating a list with all substrings
        string_list = str(ctx.message.content)[16:]

        await ctx.message.delete()

        #Getting the timer
        time = int(string_list.pop(0))

        poll_options = []
        poll_string = ''

        #Grabbing the emotes and the poll options sent with the command
        while string_list:
            poll_options.append(string_list.pop(0))
        
        #Creating the poll string        
        for i in range(0, len(poll_options), 1):
            poll_string += str(poll_options[i]) + '\n'

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
                winners.append(poll_options[aux])

        winners = [s.strip(' ') for s in winners]
        winner_message = 'Empate entre **'
        
def setup(bot):
    bot.add_cog(Bet(bot))