from discord.ext import commands
import asyncio
import random

class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #This function needs a full rewrite. Way too polluted
    @commands.command(name='votacao')
    async def start_poll(self, ctx):
        string_list = str(ctx.message.content).split(' ')
        string_list.pop(0)
        string_list.pop(0)
        poll_quantity = len(string_list)
        winners = []
        poll_emotes_count = []
        list_emotes = ['😚', '😊', '🧐', '😘', '😌', '🤓', '😗', '🤪', '😎']
        choosen_emotes = []
        await ctx.send('Escolham entre:\n')
        msg = ''

        for i in range(0, poll_quantity, 1):
            choosen_emotes.append(random.choice(list_emotes))
            list_emotes.remove(choosen_emotes[i])
            msg += choosen_emotes[i] + ' ' + string_list[i] + '\n'
        
        msg = await ctx.send(msg)
        for i in range(0, poll_quantity, 1):
            await msg.add_reaction(choosen_emotes[i])
        
        await asyncio.sleep(30)
        msg = await msg.channel.fetch_message(msg.id)
        for reaction in msg.reactions:
            poll_emotes_count.append(reaction.count)

        aux = -1
        for i in poll_emotes_count:
            aux += 1
            if i == max(poll_emotes_count):
                winners.append(string_list[aux])

        if len(winners) == 1:
            winner_message = 'Vencedor: ' + winners[0]
        else:
            for i in winners:
                winner_message = 'Empate!\nOpções empatadas: ' + ', '.join(winners)

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