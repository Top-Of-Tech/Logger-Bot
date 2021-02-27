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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="all your secret messages"))
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
    await bot.process_commands(message)

@bot.event
async def on_member_join(message):
    log.log_message(server=str(message.guild.name),
                 channel=None,
                 username=str(f'{message.name}#{message.discriminator}'),
                 message=str(f'{message.name}#{message.discriminator} - Joined')
                 )

@bot.event
async def on_member_remove(message):
    log.log_message(server=str(message.guild.name),
                 channel=None,
                 username=str(f'{message.name}#{message.discriminator}'),
                 message=str(f'{message.name}#{message.discriminator} - Left')
                 )



bot.run()