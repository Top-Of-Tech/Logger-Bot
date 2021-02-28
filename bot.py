import discord
from discord.ext import commands
import os
import log

intents = discord.Intents().all()
bot = commands.Bot("!", intents=intents)
bot.remove_command("help")

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
@bot.event
async def on_member_update(before, after):
    try:
        if before.display_name != after.display_name:
            log.log_message(server=str(before.guild.name),
                    channel=None,
                    username=str(f'{before.display_name}#{before.discriminator}'),
                    message=str(f'{before.display_name}#{before.discriminator} - Changed nickname to: {after.display_name}#{after.discriminator}'))
            log.log_rename(new_name=f'{after.guild.name}/{after.display_name}#{after.discriminator}',
                            old_name=f'{before.guild.name}/{before.display_name}#{before.discriminator}')
        elif before.raw_status != after.raw_status:
            log.log_message(server=str(before.guild.name),
                    channel=None,
                    username=str(f'{after.display_name}#{after.discriminator}'),
                    message=str(f'{after.display_name}#{after.discriminator} - Changed status from: {before.raw_status} to: {after.raw_status}'))
        elif before.activity.name != after.activity.name:
            log.log_message(server=str(before.guild.name),
                    channel=None,
                    username=str(f'{after.display_name}#{after.discriminator}'),
                    message=str(f'{after.display_name}#{after.discriminator} - Changed activaite from: {before.activity.name} to: {after.activity.name}'))
        elif len(before.roles) != len(after.roles):
            added_role = list(set(before.roles)^set(after.roles))
            log.log_message(server=str(before.guild.name),
                    channel=None,
                    username=str(f'{after.display_name}#{after.discriminator}'),
                    message=str(f'{after.display_name}#{after.discriminator} - Role added: {added_role.name}'))
    except: pass

bot.run()
