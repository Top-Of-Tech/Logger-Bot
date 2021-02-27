import discord
from discord.ext import commands
import os

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Help Command", color=0x1479d2)

        embed.add_field(name="**General**", value="`General commands`", inline=True)
        embed.add_field(name="**Moderation**", value="`Moderation commands`", inline=True)

        await ctx.send(embed=embed)

    @commands.command(aliases=["md"])
    async def moderation(self, ctx):
        embed=discord.Embed(title="**Moderation**", color=0x1479d2)
        embed.add_field(name="`!ban`", value="Bans a user", inline=False)
        embed.add_field(name="`!kick`", value="Kicks a user", inline=False)
        embed.add_field(name="`!mute`", value="Mutes a user", inline=False)
        embed.add_field(name="`!unmutes`", value="Unmutes a user", inline=False)
        embed.add_field(name="`!purge`", value="Deletes messages", inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=["gn"])
    async def general(self, ctx):
        embed=discord.Embed(title="**General**", color=0x1479d2)
        embed.add_field(name="`!help`", value="Shows help command", inline=False)
        embed.add_field(name="`!moderation`", value="Shows moderation commands", inline=False)
        embed.add_field(name="`!general`", value="This command :)", inline=False)
        embed.add_field(name="`!ping`", value="Shows bot's latency", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        latency = float(self.client.latency)
        if latency < 1:
            message = "ping is extremely good!"
        elif latency < 100:
            message = "ping is very good!"
        elif latency < 300:
            message = "ping is good!"
        elif latency < 500:
            message = "ping is ok!"
        elif latency < 1000:
            message = "ping is horrible!"
        embed=discord.Embed(title=f"Pong! The bot's {message}", color=0x1479d2)
        embed.set_footer(text=f"Ping is {round(latency, 4)} M/S")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(General(client))