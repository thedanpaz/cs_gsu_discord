from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio
import random
import os
load_dotenv()

# intents = discord.Intents.default()
# intents.members = True
# client = discord.Client(intents=intents)

intents = discord.Intents(messages=True,members = True, guilds=True)
bot = commands.Bot(command_prefix='!', intents=intents)

# class Slapper(commands.Converter):
#     async def convert(self, ctx, argument):
#         to_slap = random.choice(ctx.guild.members)
#
#         print(to_slap)
#
#         return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)

# @bot.command()
# async def slap(ctx, *, reason: Slapper):
#     await ctx.send(reason)


@bot.command()
async def command(ctx):
    # Get a Channel Object
    output = "```"
    output += "Commands for CS_GSU_BOT\n\n"
    output += "!ping - ...\n"
    output += "!fiveDolla - Collect 5 dollars for Chen. Must specify a reason.\n"
    output += "!shadowKeeper - List the current keeper of the Shadow Realm\n"
    output += "!shadowLeader - Display the fearless leader of the Shadow Realm\n"
    output += "!hothothotties - Display the eccentric supreme general of the Jalapeño Hotties\n"
    output += "!geriatricKeeper - Display the name(s) of the kind soul who has taken the oath of taking care of the elderly server members. Bless their heart\n"
    output += "!saints - Display the name(s) of the class suck-up(s)\n"
    output += "!tagSomeone - Randomly tag someone\n"
    output += "!dance - Randomly tag server member with a dance GIF\n"
    output += "!coinFlip - Flip a Coin\n"
    output += "!golfClap - Clap, Clap, Clap\n"
    output += "!pinterestRoyalty - Display the name(s) of those who pinterest like royalty\n"
    output += "!doughnuts - Display the name(s) of those who distribute the doughnuts\n"
    output += "!nerves\n"
    output += "```"
    await ctx.send(output)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def coinFlip(ctx):
    coinFace = "heads" if random.randint(0, 1) == 0 else "tails"
    await ctx.send(coinFace)

@bot.command()
async def nerves(ctx):
    # Embed Object
    em = discord.Embed(description="", colour=0xDEADBF)
    em.set_author(name="Jordan Peele", icon_url="")
    em.set_image(url="https://media.giphy.com/media/LRVnPYqM8DLag/giphy.gif")
    await ctx.send(embed=em)

@bot.command()
async def golfClap(ctx):
    # A list of dictionaries containing details about GIF's to use
    claps = [
        {"name": "",
         "avatar": "",
         "url": "https://media.giphy.com/media/XMc1Ui9rAFR1m/giphy.gif",
         "description": "It\'s not unusual, {}. It\'s just not."},
        {"name": "James Van Der Beek",
         "avatar": "",
         "url": "https://media.giphy.com/media/gRxjhVNfFgqI0/giphy.gif",
         "description": "{}, well you asked for it."},
        {"name": "John Stewart",
         "avatar": "",
         "url": "https://media.giphy.com/media/WtBDAH97eXAmQ/giphy.gif",
         "description": "I told you {}, u can\'t touch this"}
    ]

    # Get a random number that represents an available gif
    gifToUse = random.randint(0, (len(claps) - 1))

    # Embed Object
    em = discord.Embed(description="", colour=0xDEADBF)
    em.set_author(name=claps[gifToUse]['name'], icon_url=claps[gifToUse]['avatar'])
    em.set_image(url=claps[gifToUse]['url'])

    # Send the message with the EMBED
    await ctx.send(embed=em)

@bot.command()
async def tagSomeone(ctx):
    taggedUser = random.randint(0, (len(ctx.guild.members) - 1))
    i = 0
    for member in ctx.guild.members:
        if (i == taggedUser):
            # await client.send_message(message.channel, "{} is it.".format(member.mention))
            await ctx.send("{} is it.".format(member.mention))
            break
        i += 1

@bot.command()
async def fiveDolla(ctx, *, reason):
    await ctx.send(reason)

    to_slap = random.randint(0, (len(ctx.guild.members) - 1))
    i = 0
    for member in ctx.guild.members:
        if (i == to_slap):
            await ctx.send('{0.author.mention} is collecting 5 dolla from {1} for Chen because *{2}*'.format(ctx, member.mention, reason))
            break
        i += 1

@bot.command()
async def dance(ctx):
    # A list of dictionaries containing details about GIF's to use
    dances = [
        {"name": "Carlton",
         "avatar": "http://images.bwog.com/wp-content/uploads/2016/03/enhanced-buzz-28067-1364231406-0.jpg",
         "url": "https://media.giphy.com/media/cyyac9sTiN7ji/giphy.gif",
         "description": "It\'s not unusual, {}. It\'s just not."},
        {"name": "Lords of Riverdance",
         "avatar": "http://irishamerica.com/wp-content/uploads/2015/11/FT5S-Michael-Flatley-Dance-Irish-lord-front-smarm.jpg",
         "url": "https://media.giphy.com/media/87SVefpPJAo6s/giphy.gif",
         "description": "{}, well you asked for it."},
        {"name": "McHammer",
         "avatar": "http://www.notinhalloffame.com/media/k2/items/cache/a8a70130aed1b4387634a8604a34a91e_L.jpg",
         "url": "https://media.giphy.com/media/kgKrO1A3JbWTK/giphy.gif",
         "description": "I told you {}, u can\'t touch this"}
    ]

    # Default the member to mention, the author who originated the message
    memberToMention = ctx.author

    # # Random number identifying a member to Troll
    # theTrolled = random.randint(0, (len(message.server.members) - 1))

    # Variable to hold an iterator
    i = 0
    # for member in message.server.members:
    #     # Augment
    #     i += 1
    #
    #     # todo - needs to be agreed upon by other admins
    #     # if i == theTrolled:
    #     #     print("name:" + member.name)
    #     #     print("id:" + member.id)
    #     #     print("nick:" + str(member.nick))

    # Get a random number that represents an available gif
    gifToUse = random.randint(0, (len(dances) - 1))

    # Embed Object
    em = discord.Embed(description=dances[gifToUse]['description'].format(memberToMention.mention), colour=0xDEADBF)
    em.set_author(name=dances[gifToUse]['name'], icon_url=dances[gifToUse]['avatar'])
    em.set_image(url=dances[gifToUse]['url'])

    # Send the message with the EMBED
    # await client.send_message(message.channel, embed=em)
    await ctx.send(embed=em)

@bot.command()
async def shadowKeeper(ctx):
    await ctx.send( "OoOoo Shadow Keeper. Fancy.")
    for member in ctx.guild.members:
        for role in member.roles:
            # if role.id == 413888301812940802:  # shadow keeper role
            if role.name == "Keeper of the Shadow Realm":  # shadow keeper role
               await ctx.send(member.mention + " is a " + role.name)

@bot.command()
async def shadowLeader(ctx):
    for member in ctx.guild.members:
        for role in member.roles:
            if role.name == "Supreme Leader of the Shadow Realm":  # shadow keeper role
               await ctx.send("All bow to the Supreme Leader of the Shadow Realm: {}".format(member.mention))

@bot.command()
async def hothothotties(ctx):
    for member in ctx.guild.members:
        for role in member.roles:
            if role.name == "General Supremo de los Jalapeño Hotties":
               await ctx.send("I present to you, el General Supremo de los Jalapeño Hotties: {}".format(member.mention))

@bot.command()
async def geriatricKeeper(ctx):
    for member in ctx.guild.members:
        for role in member.roles:
            if role.name == "Keeper of the Geriatrics":
               await ctx.send("My liege, the Keeper of the Geriatrics: {}".format(member.mention))

@bot.command()
async def saints(ctx):
    for member in ctx.guild.members:
        for role in member.roles:
            if role.name == "Patron Saint of Sucking Up in Class":
               await ctx.send("The Mother Teresa of kiss-up's: {}".format(member.mention))

@bot.command()
async def pinterestRoyalty(ctx):
    for member in ctx.guild.members:
        for role in member.roles:
            if role.name == "Patron Saint of Pinterest":
               await ctx.send("So you are a collect snippets and fonts? eh? Hail to pinterest royalty: {}".format(member.mention))

@bot.command()
async def doughnuts(ctx):
    for member in ctx.guild.members:
        for role in member.roles:
            if role.name == "Doughnut Distributor":
               await ctx.send("Mmmmmm. Doughnuts. Thanksk for sharing: {}".format(member.mention))

@has_permissions(manage_roles=True, ban_members=True)
async def newShadowKeeper():
    await bot.wait_until_ready()

    # Background function only for Guild "GSU - CS" (377968199645396993)

    # List of phrases to "thank" a user for their service
    departingKeeper = [
        "{}, you did a okay job at keeping the shadow realm at bay. But, uh, next time...don't fall asleep on the job, then this won't have to be so awkward.",
        "Yea, uh, you're fired. Better luck next time {}.",
        "{} your services are no longer required. Please exit through the gift shop."
    ]

    # List of phrases to "welcome" a user to the their new role
    arrivingKeeper = [
        "With great power comes great responsibility {}. Best of luck keeping the shadow realm...We are not behind you.",
        "Wow, {}, I hope you can do a better job than the last person. Try to keep the shadow realm in check, for all our sake.",
        "GLHF {}. No turning back now...the shadow realm needs you."
    ]

    # Get a Channel Object
    channel = discord.utils.get(bot.get_all_channels(), guild__name='GSU - CS', name='general')

    while not bot.is_closed():

        # Determine which departing phrase to use
        departPhrasePosition = random.randint(0, (len(departingKeeper) - 1))

        # Determine which arraying phrase to use
        arrivingPhrasePosition = random.randint(0, (len(arrivingKeeper) - 1))

        # Set a list of Member Objects
        members = []

        for member in bot.get_all_members():

            # Check if the member is in guild 377968199645396993 (GS CSU)
            # if member.guild.id == "377968199645396993": # Only consider members in guild 377968199645396993 (GS CSU)
            if member.guild.name == "GSU - CS": # Only consider members in guild 377968199645396993 (GS CSU)

                # Check this member's roles
                for role in member.roles:

                    # Check if this member has the shadow keeper role
                    # if role.id == "413888301812940802":  # shadow keeper role
                    if role.name == "Keeper of the Shadow Realm":  # shadow keeper role
                        existingKeeper = member
                        shadowKeeperRole = role # todo - this should be grabbed from iterating over all server roles rather than searching for the role within a member
                        continue

                # Ensure that this member is not the BOT
                # if member.id != "413878946598486016":
                if member.name != "CS_GSU_BOT":

                    # Boolean used to determine if the member should be appended to the list of members eligible to be shadow keepers
                    appendMember = True

                    # Iterate again over the roles for a member, checking their eligibility to be Shadow Keepers
                    for role in member.roles:

                        # appendMember was already set to false, so don't check for any other role attributes
                        if appendMember == False:
                            continue

                        # if role.id == "403725126530498571": # Admin's are ineligible
                        if role.name == "admins": # Admin's are ineligible
                            appendMember = False
                            continue

                        # if role.id == "424030254093303808":  # The Supreme Leader of the Shadow Realm is ineligible
                        if role.name == "Supreme Leader of the Shadow Realm":  # The Supreme Leader of the Shadow Realm is ineligible
                            appendMember = False
                            continue

                    # Append to the list
                    if appendMember:
                        members.append(member)

        # Remove the Existing Keeper from the members list
        members.remove(existingKeeper)

        # Determine which member is going to become the new keeper
        newKeeperPosition = random.randint(0, (len(members) - 1))

        # Thank the existing keeper for their service
        await existingKeeper.remove_roles(shadowKeeperRole)

        # send a message to the channel
        await channel.send(departingKeeper[departPhrasePosition].format(existingKeeper.mention))

        # Set a new keeper
        await members[newKeeperPosition].add_roles(shadowKeeperRole)

        # Send a message to the channel
        await channel.send(arrivingKeeper[arrivingPhrasePosition].format(members[newKeeperPosition].mention))

        # Sleep for 1 day
        await asyncio.sleep(86400)  # task runs every 1 day

bot.loop.create_task(newShadowKeeper())
bot.run(os.getenv("DISCORD_TOKEN"))