import discord
from discord.ext import commands
import os
import log

intents = discord.Intents.default()
bot = commands.Bot("!", intents=intents)

print("""
 _                                  ____        _
| |    ___   __ _  __ _  ___ _ __  | __ )  ___ | |_
| |   / _ \ / _` |/ _` |/ _ \ '__| |  _ \ / _ \| __|
| |__| (_) | (_| | (_| |  __/ |    | |_) | (_) | |_
|_____\___/ \__, |\__, |\___|_|    |____/ \___/ \__|
            |___/ |___/""")

@bot.event
async def on_ready():
    print("Bot is logging and online")

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_message(message):
    log.log_message(server=str(message.guild),
                 channel=str(message.channel),
                 username=str(message.author),
                 message=str(message.content)
                 )

bot.run("ODE0OTQwNzM1MDk0NTIxOTA2.YDlKtA.6qgDOY93oHP2cYulVSGzyuy1f_E")