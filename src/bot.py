import asyncio
import sys
import time

import discord
import logger
import insta


log = logger.Logger('BOT')


REQUEST_DELAY = 10  # 5 * 60
CMD_PREFIX = "!"
INVALID_CMD_MSG = f"Invalid command. Enter '{CMD_PREFIX}help' for more info."


class Command:
    name = 'help'
    description = """
    Show the help message.
    """

    commands = {}

    def __init_subclass__(cls, **kwargs):
        cls.register()

    @classmethod
    async def run(cls, bot, req_msg: discord.Message, *args: str):
        await req_msg.reply(Command.help_msg(), mention_author=False)

    @staticmethod
    def help_msg():
        res = "Command help for bot 'ThompsonBot':\n"
        for cmd, obj in Command.commands.items():
            help_msg = f"{CMD_PREFIX}{obj.name}: {obj.description}\n"
            res += help_msg
        return res

    @classmethod
    def register(cls):
        Command.commands[cls.name] = cls


Command.register()  # register 'help' command.


class SetCommandsChannel(Command):
    name = 'command_channel'
    description = """
    Set the channel in which the bot will receive commands.
    """

    @classmethod
    async def run(cls, bot, req_msg: discord.Message, *args: str):
        if len(args) != 1:
            await req_msg.reply("Invalid arguments.", mention_author=False)
            return
        log.log("SetCommandsChannel: message =", req_msg.content)
        if not req_msg.content.startswith('!command_channel <#'):
            await req_msg.reply("Argument 1 must mention a channel.", mention_author=False)
            return
        channel_id = int(req_msg.content.removeprefix('!command_channel <#').removesuffix('>'))
        log.log("SetCommandsChannel: channel_id =", channel_id)
        bot.add_channel(channel_id, 'commands')
        await req_msg.reply(f"Bot now operates commands only on {bot.get_channel(channel_id).mention}.", mention_author=False)


class SetNewsChannel(Command):
    name = 'news_channel'
    description = """
    Configure the channel where the bot will post news from instagram.
    """

    @classmethod
    async def run(cls, bot, req_msg: discord.Message, *args: str):
        pass


class Bot(discord.Client):
    """
    The main class for the bot.
    """
    def __init__(self):
        """
        Initialize the bot instance with the intents we need.
        """
        i = discord.Intents.default()
        i.message_content = True
        super().__init__(intents=i)

        self.channels = {}
        self.last_post = None
        self.tracking = False
        self.ready = False
        # self.start_tracking()

    def add_channel(self, id_, name):
        """
        Add the given channel to registry.
        """
        self.channels[name] = id_

    def start_tracking(self):
        while not self.ready:
            pass

        asyncio.run(self.track_posts())

    async def track_posts(self):
        """
        Asynchronously track posts from the target instagram account.
        """
        self.tracking = True
        while self.tracking:
            time.sleep(REQUEST_DELAY)  # wait request delay
            if REQUEST_DELAY <= (2.5 * 60):
                time.sleep(2.5 * 60)

            post = insta.get_last_post()

            if post == self.last_post:
                continue
            self.last_post = post
            try:
                await self.channels['announcements'].send(post.get())
            except:
                self.tracking = False
                print("Exception caught while tracking instagram posts:", file=sys.stderr)
                sys.excepthook(*sys.exc_info())

    async def on_message(self, message: discord.Message):
        """
        Discord callback for when we receive a message from a user.
        Only for testing purposes and commands.
        """
        if message.author.id == self.user.id:
            return
        log.log(f"Received '{message.content}' from user '{message.author.name}', channel n°{message.channel.id}.")
        log.log("channel:", self.channels)
        if ('commands' in self.channels) and (message.channel.id != self.channels['commands']):
            return
        args = message.content.split(' ')
        cmdname = args.pop(0)
        if not cmdname.startswith(CMD_PREFIX):
            return
        cmdname = cmdname.removeprefix(CMD_PREFIX)
        if cmdname not in Command.commands:
            await message.reply(INVALID_CMD_MSG)
            return
        cmd = Command.commands[cmdname]
        await cmd.run(self, message, *args)
        """if message.author.id == self.user.id:
            return
        await message.reply('Success!')"""

    async def on_ready(self, *args):
        """
        Discord callback for when the bot is ready.
        """
        log.log("Ready!", level=logger.LOG_INFO)
        self.ready = True

