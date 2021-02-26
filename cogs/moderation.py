import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def ban(self, ctx, member: discord.Member, *, reason):
        await member.ban(reason=reason)
        embed=discord.Embed(title=f"{member.mention} was banned for: {reason}", color=0x1479d2)
        await ctx.send(embed=embed)

    async def kick(self, ctx, member: discord.Member, *, reason):
        await member.kick(reason=reason)
        embed=discord.Embed(title=f"{member.mention} was kicked for: {reason}", color=0x1479d2)
        await ctx.send(embed=embed)

    async def mute(self, ctx, member: discord.Member, *, reason):
        try:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            print(role)
            await ctx.add_roles(member, role)
            embed=discord.Embed(title=f"{member.mention} was muted for: {reason}", color=0x1479d2)
            await ctx.send(embed=embed)
        except Exception as e:
            print(e)

    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")

        if role not in member.roles:
            embed=discord.Embed(title=f"{member.mention} wasn't muted!", color=0x1479d2)
            await ctx.send(embed=embed)
        else:
            await member.remove_roles(role)
            embed=discord.Embed(title=f"{member.mention} was unmuted", color=0x1479d2)
            await ctx.send(embed=embed)

    async def purge(self, ctx, amount):
        await ctx.channel.purge(limit=amount)
        embed=discord.Embed(title=f"Purged {amount} messages", color=0x1479d2)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))