import os
import discord
from duckduckgo_search import ddg_images
from discord.ext import commands
import datetime



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)
client=commands.Bot(command_prefix="!",intents = intents)
 
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_member_join(member):
    #When a member joins the discord, they will get mentioned with this welcome message
    print(f'Member {member.mention} has joined!')

@client.command(pass_context=True)
async def serverinvte(context):
	"""DM's A Invite Code (To The Server) To The User"""
	invite = await context.channel.create_invite(context.message.guild)
	await context.send(context.message.author,",your invite URL is {}".format(invite.url))
	await context.send("Check your Dm's for the invite link")

@client.command(pass_context = True)
async def serverinfo(ctx):
    '''Displays Info About The Server!'''
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Itsy Bitsy Brasto", timestamp=datetime.datetime.utcnow(), color=discord.Color.gold())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://w7.pngwing.com/pngs/842/992/png-transparent-discord-computer-servers-teamspeak-discord-icon-video-game-smiley-online-chat-thumbnail.png")

    await ctx.send(embed=embed)


@client.command()
async def warn(ctx,user="", reason="", mod="",channel = ""):
    """Warns a Member"""
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await ctx.send("You do not have the role: Admin")
    # pass

    if user == "":
        await ctx.send("No user mentioned")
    if reason == "":
        await ctx.send("No reason entered!")
    if mod == "":
        await ctx.send("No Moderator is selected!")
    em = discord.Embed(color=0x7289DA)
    em.add_field(name='Warning', value=("You Have Been Warned -->"))
    em.add_field(name='User', value=(user))
    em.add_field(name='Reason', value=(reason))
    em.add_field(name='Moderator', value=(mod))
    await ctx.send(channel, embed=em)


#kick a member from server
@client.command(pass_context = True)
async def ban(ctx, member : discord.Member = None, reason = " "):
    """Bans specified member from the server."""
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await ctx.send("You do not have the role: Admin")
    pass

    try:
        if member == None:
            await ctx.send(ctx.message.author.mention + ", please specify a member to ban.")
            return

        else:
            await member.kick(reason = reason)
            if reason == ".":
                await ctx.send(member+ " has been banned from the server.")
            else:
                await ctx.send(member+ " has been banned from the server. Reason: " + reason + ".")
            return
    except discord.Forbidden:
        await ctx.send("You do not have the necessary permissions to ban someone.")
        return
    except discord.HTTPException:
        await ctx.send("Something went wrong, please try again.")



#clears chat
@client.command(pass_context = True)
async def clear(context,amount = 7):
    await context.channel.purge(limit = amount)


@client.command(pass_context = True)
async def meme(context,*args):
    '''posts meme url'''
    arguments = ' '.join(args)
    await context.send(ddg_images(arguments,max_results = 1)[0]['image'])
    await context.send("Here is your meme!")



client.run('YOUR TOKEN GOES HERE')
