import discord
import time


class Bot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()

        self.sandbox = 1022496382625517649
        super().__init__(intents=intents)
        self._token = 'MTAyMjQ3NzEyMDcyOTAwNjE0MA.Gif4J8.P8y5hqXSWHBNuMQqdzT8IV8A33FvhAMzD9LpwY'
        self.run()

    def run(self, *args):
        return super().run(self._token)

    async def on_message(self, message: discord.Message):
        print(message.id, self.sandbox)
        if (message.author.id == self.user.id):
            return
        await message.reply("Success!")


bot = Bot()

