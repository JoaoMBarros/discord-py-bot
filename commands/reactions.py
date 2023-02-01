from discord.ext import commands
import asyncio

class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='votacao')
    async def start_poll(self, ctx):
        # Split the command string and create a list with all substrings
        string_list = str(ctx.message.content)[17:].split("^")

        await ctx.message.delete()

        # Get the timer
        time = int(string_list.pop(0))

        poll_options = []
        emotes = []
        poll_string = ""

        # Grab the emotes and poll options sent with the command
        while string_list:
            emotes.append(string_list.pop(0).strip())
            poll_options.append(string_list.pop(0).strip())

        # Create the poll string
        for emote, option in zip(emotes, poll_options):
            poll_string += f"{emote} ➜ {option}\n"

        poll_message = await ctx.send(poll_string)

        winners = []
        emote_counts = []

        # Add reactions to the message
        for emote in emotes:
            await poll_message.add_reaction(emote)

        # Wait until the poll ends
        await asyncio.sleep(time)

        # Get the quantity of each reaction
        poll_message = await poll_message.channel.fetch_message(poll_message.id)
        for reaction in poll_message.reactions:
            emote_counts.append(reaction.count)

        # Get the winner(s)
        for emote, count in zip(emotes, emote_counts):
            if count == max(emote_counts):
                winners.append(poll_options[emotes.index(emote)])
                winner_emote = emote

        winner_message = ""
        if len(winners) == 1:
            winner_message = f"{emotes[emotes.index(winner_emote)]} {winners[0]} venceu."
        elif len(winners) == 2:
            winner_message = f"Empate entre **{winners[0]}** e **{winners[1]}**."
        else:
            winner_message = "Empate entre **"
            for i, winner in enumerate(winners):
                if i < len(winners) - 1:
                    winner_message += f"{winner}**, **"
                else:
                    winner_message = winner_message[:-6]
                    winner_message += f"** e **{winner}**."

        await ctx.send(winner_message)
        
    @commands.command(name="pingcana")
    async def send_ping_cana(self, ctx):
        # Initializes the positive and negative reaction counters
        positive_count = 0
        negative_count = 0
        
        # Sends the question message
        question_message = await ctx.channel.send('Eu devo pingar o cana?')
        
        # Adds the "yes" and "no" reactions
        await question_message.add_reaction('👍')
        await question_message.add_reaction('👎')
        
        # Waits 15 seconds
        await asyncio.sleep(15)
        
        # Updates the message with the new reactions
        question_message = await question_message.channel.fetch_message(question_message.id)
        
        # Counts the positive and negative reactions
        for reaction in question_message.reactions:
            if reaction.emoji == '👍':
                positive_count = reaction.count - 1
            if reaction.emoji == '👎':
                negative_count = reaction.count - 1
        
        # Checks which option received the most votes
        if positive_count > negative_count:
            await ctx.channel.send("<@383320582336413706>")
        else:
            await ctx.channel.send("Não foi dessa vez")   

async def setup(bot):
    await bot.add_cog(Reactions(bot))