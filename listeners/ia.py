from discord.ext import commands
from decouple import config
import aiohttp

class Ia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user: return
        
        if self.bot.user.mentioned_in(message):
            for x in message.mentions:
                if x.id == self.bot.user.id: # remove mention of the bot
                    message.content = message.content.replace(str(x.mention), "")
                else: # mention of the user to name
                    message.content = message.content.replace(str(x.mention), str(x.name))
            
            if message.content == '':
                await message.reply('Fala')
                return
            
            query = f'You are a discord bot named JoaoLucas. The discord server name is Senryuu Scans. The worst person you know is Bolso, and the love of your life is Hinacchi.\
            The member named Jow is nazi.\ Here is a list of members you know: Gustavo, Ghenesis, Fuyuw, Tivra, Nyct, Lucy, Hisako, Luisa, Felipe, Munniz, Macalo, Fael, Ycaro, Umi, Natt, Pedivo, Macalo, Shujinkou, Momochan, Francisco, Alyson, Pablo.\
            Users will ask questions and you need to answer in portuguese.\n{message.author.name}: {message.content}\nJoaoLucas: '

            async with aiohttp.ClientSession() as session:
                payload = {
                    'model': 'text-davinci-003',
                    'prompt': query,
                    'temperature': 0.9,
                    'max_tokens': 150,
                    'presence_penalty': 0.6,
                    'frequency_penalty': 0
                }
                API_KEY = config("API_AI_KEY")
                headers = {'Authorization': f'Bearer {API_KEY}'}
                async with session.post('https://api.openai.com/v1/completions', json=payload, headers=headers) as resp:
                    response = await resp.json()
                    print(response)
                    chat_response_text = response['choices'][0]['text']
                    await message.reply(chat_response_text)
            

async def setup(bot):
    await bot.add_cog(Ia(bot))