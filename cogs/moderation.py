import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason):
        await member.ban(reason=reason)
        embed=discord.Embed(title=f"{member} was banned for: {reason}", color=0x1479d2)
        await ctx.send(embed=embed)

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason):
        await member.kick(reason=reason)
        embed=discord.Embed(title=f"{member} was kicked for: {reason}", color=0x1479d2)
        await ctx.send(embed=embed)

    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, reason):
        try:
            role = discord.utils.get(member.guild.roles, name="Muted")
            print(role)
            await member.add_roles(role)
            embed=discord.Embed(title=f"{member} was muted for: {reason}", color=0x1479d2)
            await ctx.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")

        if role not in member.roles:
            embed=discord.Embed(title=f"{member} wasn't muted!", color=0x1479d2)
            await ctx.send(embed=embed)
        else:
            await member.remove_roles(role)
            embed=discord.Embed(title=f"{member} was unmuted", color=0x1479d2)
            await ctx.send(embed=embed)

    @commands.command()
    async def purge(self, ctx, amount):
        await ctx.channel.purge(limit=int(amount))
        embed=discord.Embed(title=f"Purged {amount} messages", color=0x1479d2)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))