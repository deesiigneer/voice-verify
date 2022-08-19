import nextcord
import logging
from nextcord.ext import commands
from nextcord.flags import Intents
from os import environ, listdir
from buttons.verification import verification

logging.basicConfig(level=logging.DEBUG)


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_views_added = False

        for fn in listdir("./cogs"):
            if fn.endswith(".py"):
                self.load_extension(f"cogs.{fn[:-3]}")

    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_view(verification())
            self.persistent_views_added = True

        await self.change_presence(
            activity=nextcord.Activity(
                type=nextcord.ActivityType.watching,
                name='t.me/deesiigneer'),
            status=nextcord.Status.online)
        print(f'Logged in as {self.user} (ID: {self.user.id})')


client = Bot(intents=Intents.all())
client.run(environ.get('BOT_TOKEN', None))
