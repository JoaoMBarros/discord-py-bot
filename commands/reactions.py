from discord.ext import commands
import asyncio

class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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