from discord.ext import commands
from unidecode import unidecode

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
                    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if 'gremio' in str(unidecode(message.content)).casefold():
            await message.channel.send('<:anime:749023956987805709>')

def setup(bot):
    bot.add_cog(Meme(bot))