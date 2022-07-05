import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print("Client is online.")

@client.event
async def on_raw_reaction_add(payload):
        channel = client.get_channel("""id of the channel where you want to set the notifier""")
        if payload.user_id == """the user id you want to track""":
            GUILDID = 'server id of the target user'
            CHANNELID = payload.channel_id
            MESSAGEID = payload.message_id
            url = f"https://discord.com/channels/%7BGUILDID%7D/%7BCHANNELID%7D/%7BMESSAGEID%7D"
            await channel.send(f"Target user add a reaction {payload.emoji} on the message!\n{url}")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    channel = client.get_channel("""id of the channel where you want to set the notifier""")
    if msg.author.id  == """the user id you want to track""":
            GUILDID = 'server id of the target user'
            CHANNELID = msg.channel.id
            MESSAGEID = msg.id
            url = f"https://discord.com/channels/"+str(GUILDID)+"/"+str(CHANNELID)+"/"+str(MESSAGEID)
            if len(msg.attachments) == 0:
                await channel.send(f"Target user said: \"{msg.content}\"\n{url}")
            else :
                await channel.send(f"Target user said: \"{msg.content}\"\n")
                for item in msg.attachments:
                    await channel.send(f"{item}")
                await channel.send(f"\n{url}")

client.run('token of the client you want to use as a bot')