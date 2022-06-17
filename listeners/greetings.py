from discord.ext import commands
from datetime import datetime, timedelta

class Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('funcionando')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        current = time()
        author = message.author.name
        m = message.content
        m = str(m).casefold()

        match m:
            case 'bom dia':
                if(current == 'manha'):
                    await message.channel.send('muito bom dia, ' + author)
                else:
                    await message.channel.send('se não fosse vagabundo não tava falando bom dia essas horas')
            case 'boa tarde':
                if(current == 'tarde'):
                    await message.channel.send('muito boa tarde, ' + author)
                else:
                    await message.channel.send('isso é hora de boa tarde?')
            case 'boa noite':
                if(current == 'noite'):
                    await message.channel.send('muito boa noite, ' + author)
                else:
                    await message.channel.send('isso é hora de boa noite?')

def time():
    current = datetime.now()
    if(current.hour > 4 and current.hour <= 12):
        return 'manha'
    elif(current.hour >= 13 and current.hour <= 18):
        return ('tarde')
    return 'noite'

def setup(bot):
    bot.add_cog(Listeners(bot))