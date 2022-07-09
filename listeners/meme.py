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
                winner_string = 'PAROU! ALGUÉM CONSEGUIU! VENCEDOR(A): <@' + str(message.author.id) + '>'
                await message.channel.send('<@383320582336413706>\n' + winner_string)
                await self.bot.close()
            elif number < 177024 and number > 177002:
                await message.channel.send('Caralho,' + str(message.author.id) + ', passou muito perto kkkkkkkk. Teu número foi: ' + number)
                await message.channel.send('https://cdn.discordapp.com/attachments/725529603350855690/990102214901121114/videoplayback.mp4')
            else:
                roulette = ['🤤', '😋', 'oi', 'opa', 'quero', 'cade', 'onde', 'maconha?']
                await message.channel.send(random.choice(roulette))
            
        elif 'hg' in str(message.content).casefold():
            await message.channel.send('Hg só quando o Grêmio ganhar')
        
        elif 'jow' == str(message.content).casefold():
            await message.channel.send('https://cdn.discordapp.com/attachments/987500208407597116/995153757149077535/jow.png')

def setup(bot):
    bot.add_cog(Meme(bot))