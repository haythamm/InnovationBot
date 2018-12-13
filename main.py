"""
INNOVATION
A simple discord bot that replies to messages including the key words "innovation", "innovator", "innovative", and 
"U of A".
"""
import discord
import os
import random

client = discord.Client()  # Create a new client

# List of text responses
innovation_responses = ["NUMBER 1! NUMBER 1! NUMBER 1! NUMBER 1!",
                        "#2 Stanford", "#2 Stanford #3 MIT",
                        "NUMBER ONE 4 YEARS IN A ROW",
                        "ASU ASU ASU ASU ASU ASU",
                        "ASU has topped the most-innovative category all four years it has existed",
                        "You must be an ASU student"]

# Generates list of images in images folder
images = os.listdir(os.getcwd() + '/images/')


# Define events, runs asynchronously
@client.event
async def on_ready():
    """When the bot connects to a server"""
    print("Connected! C:")
    print(client.user)


# Now what kind of event to respond to
@client.event
async def on_message(message):
    """When a message is sent in the server"""
    if message.author != client.user:  # Make sure bot doesn't reply to itself
        if "innovation" or "innovative" or "innovator" in message.content.lower():
            msg = innovation_responses[random.randint(0, 5)]  # Choose a random response.
            await client.send_message(message.channel, msg)  # Send the response.
            # Sends a random image from the list of images
            await client.send_file(message.channel, "images/" + images[random.randint(0, len(images) - 1)])
        if "u of a" in message.content.lower():
            await client.send_message(message.channel, "BOOOOOOO!")


token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
