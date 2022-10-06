import os
import src._env as _env

import discord
from src.bot import Bot


bot = Bot()
bot.add_channel(1022494749560684554, 'sandbox')
bot.run(os.environ.get('TOKEN'))

