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
async def newShadowKeeper():
    await client.wait_until_ready()

    # List of phrases to "thank" a user for their service
    departingKeeper = [
        "{}, you did a okay job at keeping the shadow realm at bay. But, uh, next time...don't fall asleep on the job, then this won't have to be so awkward.",
        "Yea, uh, you're fired. Better luck next time {}.",
        "{} your services are no longer required. Please exit through the gift shop."
    ]

    # List of phrases to "welcome" a user to the their new role
    arrivingKeeper = [
        "With great power comes great responsibility {}. Best of luck keeping the shadow realm...We are not behind you.",
        "Wow, {}, I hope you can do a better job than the last guy. Try to keep the shadow realm in check, for all our sake.",
        "GLHF {}. No turning back now...the shadow realm needs you."
    ]

    # Get an Channel Object
    channel = discord.Object(id='416055843470049300') # Sandbox - 416055843470049300 todo - should target general when not in testing mode

    while not client.is_closed:

        # todo - Copy an instance of departingKeeper and arrivingKeeper, that unsets the phrases previously used
        # todo - will also need to reindex the instances

        # Set a list of Member Objects
        members = []

        for member in client.get_all_members():

            # Check this member's roles
            for role in member.roles:
                # Check if this member has the shadow keeper role
                if role.id == "413888301812940802":  # shadow keeper role
                    existingKeeper = member
                    shadowKeeperRole = role # todo - this should be grabbed from iterating over all server roles rather than searching for the role within a member
                    continue

            # Ensure that this member is not the BOT
            if member.id != "413878946598486016":
                # Append to the list
                members.append(member)

        # Remove the Existing Keeper from the members list
        members.remove(existingKeeper)

        # Determine which member is going to become the new keeper
        newKeeperPosition = random.randint(0, (len(members) - 1))

        # Thank the existing keeper for their service
        await client.remove_roles(existingKeeper, shadowKeeperRole)

        # Determine which departing phrase to use
        departPhrasePosition = random.randint(0, (len(departingKeeper) - 1))

        await client.send_message(channel, departingKeeper[departPhrasePosition].format(existingKeeper.name)) # todo - replace with a mention when outside of test

        # Set a new keeper
        await client.add_roles(members[newKeeperPosition], shadowKeeperRole)

        # Determine which arraying phrase to use
        arrivingPhrasePosition = random.randint(0, (len(arrivingKeeper) - 1))

        # Send a message to the channel
        await client.send_message(channel, arrivingKeeper[arrivingPhrasePosition].format(members[newKeeperPosition].name)) # todo - replace with a mention when outside of test

        # Sleep for 1 day
        await asyncio.sleep(86400)  # task runs every 1 day


@client.event
async def on_message(message):
    if message.content.startswith('!shadowKeeper'):
        await client.send_message(message.channel, "OoOoo Shadow Keeper. Fancy.")
        for member in message.server.members:
            for role in member.roles:
                if role.id == "413888301812940802": #shadow keeper role
                    await client.send_message(message.channel, member.mention + " is a " + role.name)
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

# todo - uncomment when ready for primetime client.loop.create_task(newShadowKeeper())
client.run(cfg.DISCORD['token'])