import os
import discord
import src._env
from src.bot import Bot


bot = Bot()
bot.add_channel(1022494749560684554, 'sandbox')
bot.run(os.environ.get('TOKEN'))

