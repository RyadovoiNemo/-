import os
from dotenv import load_dotenv
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="!",
                   intents=disnake.Intents.all(),
                   activity=disnake.Game('VS code',
                                         status=disnake.Status.online))
bot.remove_command('help')
bot.load_extension('cogs.comands')
bot.load_extension('cogs.events')


load_dotenv()
token = os.getenv('TOKEN')
bot.run(token)
