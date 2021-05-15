from asyncio.base_events import _MIN_SCHEDULED_TIMER_HANDLES
import discord
import json
import requests
import threading
import asyncio

class MyDiscord(discord.Client):
    def __init__(self):
        try:
            self.loopprinc = asyncio.get_event_loop()
        except RuntimeError:
            self.loopprinc = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loopprinc)

        self.loop = self.loopprinc
        super().__init__(intents=discord.Intents.all())

    # Returns asynchronous event loop
    def getLoop(self):
        return self.loopprinc

    """
    def launch(self):
        self.client.run(self.TOKEN)
    """

    # Returns Member object from userID (ex: Pere#6521)
    async def getUser(self, userID):
        l = userID.split('#')
        for mem in self.get_all_members():
            if mem.name == l[0] and mem.discriminator == l[1]:
                return mem

    # Auxiliar async function to send the message
    async def sendAsync(self, fromMail, toID, dedication):
        toU = await self.getUser(toID)

        if not dedication:
            await toU.send(":partying_face: {} wishes you a nice day! :partying_face:".format(fromMail))
        else:
            await toU.send("{} has a message for you: {}".format(fromMail, dedication))  

    # Sends a discord message to an specific user with an optional dedication.
    def enviarMSG(self, fromMail, toID, dedication):
        if not fromMail:
            fromMail = "Someone"
        asyncio.run_coroutine_threadsafe(self.sendAsync(fromMail, toID, dedication), self.loopprinc)

    # Function called when the bot logs in Discord servers.
    async def on_ready(self):
        print("Bot iniciado como {}".format(self.user))

