import config as cfg
import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Defines a background job to appoint a new shadow keeper
async def guildChecker():
    await client.wait_until_ready()
    while not client.is_closed:
        print("stuff")

        for server in client.servers:
            if(server.id == "377968199645396993"): # GSU-CS guild
                print(server.name)


        await asyncio.sleep(10)

async def newShadowKeeper():
    await client.wait_until_ready()

    # only if this it he GSU-CS guild 377968199645396993

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
    channel = discord.Object(id='377968199645396995') # Sandbox - 416055843470049300 # General 377968199645396995

    while not client.is_closed:

        # Determine which departing phrase to use
        departPhrasePosition = random.randint(0, (len(departingKeeper) - 1))

        # Determine which arraying phrase to use
        arrivingPhrasePosition = random.randint(0, (len(arrivingKeeper) - 1))

        # Set a list of Member Objects
        members = []

        for member in client.get_all_members():

            # Check if the member is in guild 377968199645396993 (GS CSU)
            if member.server.id == "377968199645396993": # Only consider members in guild 377968199645396993 (GS CSU)

                # Check this member's roles
                for role in member.roles:

                    # Check if this member has the shadow keeper role
                    if role.id == "413888301812940802":  # shadow keeper role
                        existingKeeper = member
                        shadowKeeperRole = role # todo - this should be grabbed from iterating over all server roles rather than searching for the role within a member
                        continue

                # Ensure that this member is not the BOT
                if member.id != "413878946598486016":

                    # Boolean used to determine if the member should be appended to the list of members eligible to be shadow keepers
                    appendMember = True

                    # Iterate again over the roles for a member, checking their eligibility to be Shadow Keepers
                    for role in member.roles:

                        # appendMember was already set to false, so don't check for any other role attributes
                        if appendMember == False:
                            continue

                        if role.id == "403725126530498571": # Admin's are ineligible
                            appendMember = False
                            continue

                        if role.id == "424030254093303808":  # The Supreme Leader of the Shadow Realm is ineligible
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
        await client.remove_roles(existingKeeper, shadowKeeperRole)

        # send a message to the channel
        await client.send_message(channel, departingKeeper[departPhrasePosition].format(existingKeeper.mention))

        # Set a new keeper
        await client.add_roles(members[newKeeperPosition], shadowKeeperRole)

        # Send a message to the channel
        await client.send_message(channel, arrivingKeeper[arrivingPhrasePosition].format(members[newKeeperPosition].mention))

        # Sleep for 1 day
        # await asyncio.sleep(86400)  # task runs every 1 day
        await asyncio.sleep((3600 * 12))  # task runs every 12 hours

@client.event
async def on_message(message):
    if message.content.startswith('!command'):
        # Get a Channel Object
        output = "```"
        output += "Commands for CS_GSU_BOT\n\n"
        output += "!shadowKeeper - List the current keeper of the Shadow Realm\n"
        output += "!shadowLeader - Display the fearless leader of the Shadow Realm\n"
        output += "!hothothotties - Display the eccentric supreme general of the Jalapeño Hotties\n"
        output += "!geriatricKeeper - Display the name(s) of the kind soul who has taken the oath of taking care of the elderly server members. Bless their heart\n"
        output += "!saints - Display the name(s) of the class suck-up(s)\n"
        output += "!tagSomeone - Randomly tag someone\n"
        output += "!dance - Randomly tag server member with a dance GIF\n"
        output += "```"

        await client.send_message(message.channel, output)

    elif message.content.startswith('!shadowKeeper'):
        await client.send_message(message.channel, "OoOoo Shadow Keeper. Fancy.")
        for member in message.server.members:
            for role in member.roles:
                if role.id == "413888301812940802": #shadow keeper role
                    await client.send_message(message.channel, member.mention + " is a " + role.name)
    elif message.content.startswith('!shadowLeader'):
        for member in message.server.members:
            for role in member.roles:
                if role.id == "424030254093303808":  # supreme leader of the shadow realm role
                    await client.send_message(message.channel, "All bow to the Supreme Leader of the Shadow Realm: {}".format(member.mention))
    elif message.content.startswith('!hothothotties'):
        for member in message.server.members:
            for role in member.roles:
                if role.id == "433322637180272640":  # General Supremo de los Hotties
                    await client.send_message(message.channel, "I present to you, el General Supremo de los Jalapeño Hotties: {}".format(member.mention))
    elif message.content.startswith('!tagSomeone'):
        taggedUser = random.randint(0, (len(message.server.members) - 1))
        i = 0
        for member in message.server.members:
            if(i == taggedUser):
                await client.send_message(message.channel, "{} is it.".format(member.mention))
                break
            i += 1
    elif message.content.startswith('!geriatricKeeper'):
        for member in message.server.members:
            for role in member.roles:
                if role.id == "415557846810492950":  # geriatric keeper role
                    await client.send_message(message.channel, "My liege, the Keeper of the Geriatrics: {}".format(member.mention))
    elif message.content.startswith('!saints'):
        for member in message.server.members:
            for role in member.roles:
                if role.id == "418620468065730561":  # Patron Saint of Suck Up ub Class
                    await client.send_message(message.channel, "The Mother Teresa of kiss-up's: {}".format(member.mention))
    elif message.content.startswith('!dance'):
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
        memberToMention = message.author

        # Random number identifying a member to Troll
        theTrolled = random.randint(0, (len(message.server.members) - 1))

        # Variable to hold an iterator
        i = 0
        for member in message.server.members:
            # Augment
            i += 1

            # todo - needs to be agreed upon by other admins
            # if i == theTrolled:
            #     print("name:" + member.name)
            #     print("id:" + member.id)
            #     print("nick:" + str(member.nick))

        # Get a random number that represents an available gif
        gifToUse = random.randint(0, (len(dances) - 1))

        # Embed Object
        em = discord.Embed(description=dances[gifToUse]['description'].format(memberToMention.mention), colour=0xDEADBF)
        em.set_author(name=dances[gifToUse]['name'], icon_url=dances[gifToUse]['avatar'])
        em.set_image(url=dances[gifToUse]['url'])

        # Send the message with the EMBED
        await client.send_message(message.channel, embed=em)

# client.loop.create_task(guildChecker())
client.loop.create_task(newShadowKeeper()) # Run the newShadowKeeper on loop
client.run(cfg.DISCORD['token'])