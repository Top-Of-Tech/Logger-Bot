import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # ---------------------------------------------------

    # Bans somebody
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason):
        await member.ban(reason=reason)
        embed = discord.Embed(title=f"{member} was banned for {reason}", color=0x1479d2)
        await ctx.send(embed=embed)
        await member.send(f"You were banned for {reason}")

    # ---------------------------------------------------

    # Kicks somebody
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason):
        await member.kick(reason=reason)
        embed = discord.Embed(title=f"{member} was kicked for {reason}", color=0x1479d2)
        await ctx.send(embed=embed)
        await member.send(f"You were kicked for {reason}")

    # ---------------------------------------------------

    # Mutes somebody
    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, reason):
        role = discord.utils.get(member.guild.roles, name="Muted")
        
        if role not in member.roles:
            await member.add_roles(role)
            embed = discord.Embed(title=f"{member} was muted for {reason}", color=0x1479d2)
            await ctx.send(embed=embed)
            await member.send(f"You were muted for {reason}")
        else:
            embed = discord.Embed(title=f"{member} was already muted", color=0x1479d2)
            await ctx.send(embed=embed)
    
    # ---------------------------------------------------

    # Unmutes somebody
    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")

        if role not in member.roles:
            embed = discord.Embed(title=f"{member} wasn't muted!", color=0x1479d2)
            await ctx.send(embed=embed)
        else:
            await member.remove_roles(role)
            embed = discord.Embed(title=f"{member} was unmuted", color=0x1479d2)
            await ctx.send(embed=embed)
            await member.send("You were unmuted!")

    # ---------------------------------------------------

    # Clears messages
    @commands.command()
    async def purge(self, ctx, amount):
        await ctx.channel.purge(limit=int(amount))
        embed = discord.Embed(title=f"Purged {amount} messages", color=0x1479d2)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))