import discord
from discord.ext import commands
import asyncio

class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    # ---------------------------------------------------

    # Handle command errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): # Handles error if you are missing permissions
            embed = discord.Embed(title="You are missing the permissions to use this command", color=0x1479d2)
            message = await ctx.send(embed=embed)
            await asyncio.sleep(5)
            await message.delete()

        elif isinstance(error, commands.MissingRequiredArgument): # Handles error if you are missing required arguments
            embed = discord.Embed(title="You are missing a required argument for this command", color=0x1479d2)
            message = await ctx.send(embed=embed)
            await asyncio.sleep(5)
            await message.delete()

        elif isinstance(error, commands.CommandNotFound): # Handles error if the command is not found
            embed = discord.Embed(title="This command does not exist", color=0x1479d2)
            message = await ctx.send(embed=embed)
            await asyncio.sleep(5)
            await message.delete()

    
def setup(client):
    client.add_cog(Errors(client))