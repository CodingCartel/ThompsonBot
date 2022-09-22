import os
import _env

import discord
import time


class Bot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()

        self.sandbox = 1022496382625517649
        super().__init__(intents=intents)
        self._token = os.environ.get('TOKEN')
        self.run()

    def run(self, *args):
        return super().run(self._token)

    async def on_message(self, message: discord.Message):
        print(message.id, self.sandbox)
        if (message.author.id == self.user.id):
            return
        await message.reply("Success!")


bot = Bot()

