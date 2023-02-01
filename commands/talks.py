import random
import requests
import asyncio
from translate import Translator
from discord.ext import commands
from discord import app_commands



class Talks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def sync(self, ctx) -> None:
        synced = await ctx.bot.tree.sync()
        await ctx.send(
            f"Synced {len(synced)} commands to the current guild."
        )
        return
        
    @commands.command(name='contebaixo')
    async def count_down(self, ctx):
        # Split the command string at the space character
        numbers = str(ctx.message.content)[20:].split(' ')

        if len(numbers) == 2:
            # Convert the second number to an integer and decrement it by 1
            floor_number = int(numbers[1]) - 1
            # Convert the first number to an integer
            ceiling_number = int(numbers[0])

            # Delete the original command message
            await ctx.message.delete()
            # Send a message indicating that the countdown has started
            await ctx.send('Contando...')

            # Count down from ceiling_number to floor_number (inclusive)
            for count in range(ceiling_number, floor_number, -1):
                # Send the current count and delete it after 1 second
                await ctx.send(count, delete_after=1.0)
                # Sleep for 1 second before continuing the loop
                await asyncio.sleep(1)

            # Calculate the number of seconds passed
            seconds_passed = ceiling_number - floor_number
            # Send a message indicating the number of seconds passed
            await ctx.send(f'Contei {seconds_passed} segundos')
        else:
            # If there are not enough numbers, send a message indicating this
            await ctx.send('Mande 2 números')
            
    @commands.command(name='contecima')
    async def count_up(self, ctx):
        # Split the command string at the space character
        numbers = str(ctx.message.content)[19:].split(' ')

        if len(numbers) == 2:
            # Convert the first number to an integer
            floor_number = int(numbers[0])
            # Convert the second number to an integer and increment it by 1
            ceiling_number = int(numbers[1]) + 1
            # Delete the original command message
            await ctx.message.delete()
            # Send a message indicating that the countdown has started
            await ctx.send('Contando...')

            # Count up from floor_number to ceiling_number (inclusive)
            for count in range(floor_number, ceiling_number):
                # Send the current count and delete it after 1 second
                await ctx.send(count, delete_after=1.0)
                # Sleep for 1 second before continuing the loop
                await asyncio.sleep(1)

            # Calculate the number of seconds passed
            seconds_passed = ceiling_number - floor_number
            # Send a message indicating the number of seconds passed
            await ctx.send(f'Contei {seconds_passed} segundos')
        else:
            # If there are not enough numbers, send a message indicating this
            await ctx.send('Mande 2 números')

    @commands.hybrid_command(name='repita')
    async def send_message_again(self, ctx, text: str):
        # Split the command string and remove the first two elements
        string_list = str(ctx.message.content).split(' ')[2:]
        
        # Join the remaining elements to create the response string
        response = ' '.join(string_list)
        
        # Delete the original message and send the response
        #await ctx.message.delete()
        await ctx.send(text)

    @commands.command(name='qual')
    async def send_message_choose(self, ctx):
        # Split the command string at 'ou' and store the options in a list
        options = str(ctx.message.content)[14:].split(' ou ')

        # Choose a random option and create the response message
        response = f'Na minha opinião, {random.choice(options)}.'

        # Send the response message
        await ctx.send(response)

    @commands.command(name='diga')
    async def send_message_yes_or_no(self, ctx):
        # Create a list of possible answers
        answers = ['Sim', 'Não', 'De forma alguma', 'Não sei', 'Com toda certeza']

        # Choose a random answer
        response = random.choice(answers)

        # Send the response message
        await ctx.send(response)

    @commands.command(name='sabio')
    async def send_message_sabio(self, ctx):
        # Create a translator object to translate the text to Portuguese
        translator = Translator(to_lang='pt')

        # Send a GET request to the API and store the response
        response = requests.get('https://api.adviceslip.com/advice')

        # Convert the response to a dictionary
        advice_json = response.json()

        # Get the advice from the dictionary
        advice = advice_json['slip']['advice']

        # Delete the command message
        await ctx.message.delete()

        # Translate the advice to Portuguese and send it as the response message
        await ctx.send(translator.translate(advice))
    
    @commands.hybrid_command(name='convite')
    async def send_message_convite(self, ctx, text: str):
        # Set the response message to be the invite link
        response = 'https://discord.gg/DCz9WNf'

        # Delete the command message
        await ctx.message.delete()

        # Send the response message
        await ctx.send(response)

    @commands.command(name='roteiro')
    async def send_message_roteiro(self, ctx):
        # Generate a random percentage
        percentage = random.randint(0, 99)

        # Create the response message
        response = f'O roteiro está {percentage}% pronto'

        # Send the response message
        await ctx.send(response)

    @commands.command(name='cap')
    async def send_message_cap(self, ctx):
        # Set the response message
        response = 'Não se preocupe que em breve sairão alguns capítulos. Parte da equipe está bem atarefada ou com outros projetos ou com problemas pessoais/escola/universidade/trabalho, aí o processo é mais lento do que já era.' \
                ' Se não quiser ler em inglês, tem um pessoal no facebook que fazia a tradução deles, e até onde eu lembro, era bem rápida. Não faço ideia de onde eles pegam a tradução ou da qualidade deles, mas deve ajudar se o seu inglês não for afiado. Aí você decide se quer revisitar o nosso mais tarde ou não.\n\n' \
                'Mas não se preocupe que não paramos de fazer não, só estamos mais ocupados e não queremos cortar a qualidade por conta disso. Espero que entenda'

        # Delete the command message
        await ctx.message.delete()
        
        # Send the response message
        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(Talks(bot))