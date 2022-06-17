from discord.ext import commands
import asyncio

class Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("funcionando")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if "roteiro" in message.content:
            await message.channel.send("to fazendo")

        if message.content.startswith("cade o cap"):
            channel = message.channel
            await channel.send("cade de que")

            def check(m):
                r = m.content
                r = str(r).lower()
                return r == "kaguya"

            try:
                await self.bot.wait_for('message', timeout = 10.0, check=check)
            except asyncio.TimeoutError:
                await channel.send("demorou demais")
            else:
                await channel.send("ta saindo")
                    
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(Listeners(bot))