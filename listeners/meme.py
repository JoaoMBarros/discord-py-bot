import random
from discord.ext import commands
from unidecode import unidecode
import json

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
                    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        lowercase_message = message.content.casefold()

        # Verifica mensagens exatas
        if 'gremio' == str(unidecode(lowercase_message)):
            await message.channel.send('<:anime:749023956987805709>')
        
        elif 'flamengo' == lowercase_message:
            await message.channel.send('silencio, deixem o mestre vitor pereira trabalhar')
        
        elif 'hg' == lowercase_message:
            await message.channel.send('Hg só quando o Grêmio ganhar')
        
        elif 'jow' == lowercase_message:
            await message.channel.send('https://cdn.discordapp.com/attachments/987500208407597116/995153757149077535/jow.png')
        
        elif 'e a japa luisa' == lowercase_message:
            await message.channel.send('ainda na luta')
        
        # Verifica se certa palavra foi mencionada na mensagem
        elif 'maconha' in lowercase_message:
            target = 177013
            number = random.randint(0, 500000)

            if number == target:
                winner_string = f'PAROU! ALGUÉM CONSEGUIU! VENCEDOR(A): <@{message.author.id}>'
                await message.channel.send('<@383320582336413706>\n' + winner_string)
                await self.bot.close()
            elif number < 177024 and number > 177002:
                await message.channel.send(f'Caralho, {message.author.id}, passou muito perto kkkkkkkk. Teu número foi: {number}')
                await message.channel.send('https://cdn.discordapp.com/attachments/725529603350855690/990102214901121114/videoplayback.mp4')
            else:
                roulette = ['🤤', '😋', 'oi', 'opa', 'quero', 'cade', 'onde', 'maconha?', 'https://media.discordapp.net/attachments/658011749857099799/1058048872905191537/1247.png?width=473&height=473']
                await message.channel.send(random.choice(roulette))

        elif 'sexo' in lowercase_message:
            await message.channel.send('<:sexo:993607518750261328>')

async def setup(bot):
    await bot.add_cog(Meme(bot))