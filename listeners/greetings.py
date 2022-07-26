import pytz
from discord.ext import commands
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

class Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('funcionando')
        
        #Trigger the send_midnight_message every day at 0:00:00
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.send_midnight_message, CronTrigger(hour='0', minute='00', second='00', timezone='America/Sao_Paulo'))
        scheduler.add_job(self.send_4_20_message, CronTrigger(hour='4', minute='20', second='00', timezone='America/Sao_Paulo'))
        scheduler.add_job(self.send_16_20_message, CronTrigger(hour='16', minute='20', second='00', timezone='America/Sao_Paulo'))
        scheduler.start()

    async def send_midnight_message(self):
        c = self.bot.get_channel(658011360625688587)
        await c.send('Meia noite, hora da maldade')
    
    async def send_4_20_message(self):
        c = self.bot.get_channel(988536738987266108)
        await c.send('Mamãe dormiu, fumaça subiu')
    
    async def send_16_20_message(self):
        c = self.bot.get_channel(988536738987266108)
        await c.send('Hora do chá')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        current = time()
        author = message.author.name

        match str(message.content).casefold():
            case 'bom dia':
                if(current == 'manha'):
                    await message.channel.send('muito bom dia, ' + author)
                else:
                    await message.channel.send('se não fosse vagabundo não tava falando bom dia essas horas')
            case 'boa tarde':
                if(current == 'tarde'):
                    await message.channel.send('muito boa tarde, ' + author)
                else:
                    await message.channel.send('acha que pai de familia ta dando boa tarde essas horas?')
            case 'boa noite':
                if(current == 'noite'):
                    await message.channel.send('muito boa noite, ' + author)
                else:
                    await message.channel.send('isso é hora de boa noite?')
            

def time():
    current = datetime.now(pytz.timezone('America/Sao_Paulo'))
    
    if current.hour == 12 and current.minute == 00 and current.second == 00:
        return 'meia_noite'
    if(current.hour > 4 and current.hour < 13):
        return 'manha'
    elif(current.hour > 12 and current.hour < 19):
        return 'tarde'
    return 'noite'

def setup(bot):
    bot.add_cog(Listeners(bot))