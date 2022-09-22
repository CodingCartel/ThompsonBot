import discord
import logger


log = logger.Logger('BOT')


class Bot(discord.Client):
    def __init__(self):
        i = discord.Intents.default()
        # i.message_content = True
        super().__init__(intents=i)

        self.channels = {}

    def add_channel(self, id_, name):
        self.channels[name] = id_

    async def on_message(self, message: discord.Message):
        if message.author.id == self.user.id:
            return
        await message.reply('Success!')

    async def on_ready(self, *args):
        log.log("Ready!", level=logger.LOG_INFO)

