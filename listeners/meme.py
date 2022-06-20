import random
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
            
        elif 'flamengo' in str(message.content).casefold():
            await message.channel.send('silencio, deixem o mestre dorival trabalhar')
            
        elif 'maconha' in str(message.content).casefold():
            target = 177013
            number = random.randint(0, 500000)
            if number == target:
                await message.channel.send('<@383320582336413706>')
            else:
                roulette = ['oi', 'opa', 'quero', 'cade', 'onde']
                await message.channel.send(random.choice(roulette))
            
        elif 'hg' in str(message.content).casefold():
            await message.channel.send('Hg só quando o Grêmio ganhar')

def setup(bot):
    bot.add_cog(Meme(bot))