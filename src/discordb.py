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

    def getLoop(self):
        return self.loopprinc

    """
    def launch(self):
        self.client.run(self.TOKEN)
    """

    async def getUser(self, userID):
        l = userID.split('#')
        for mem in self.get_all_members():
            if mem.name == l[0] and mem.discriminator == l[1]:
                return mem

    async def sendAsync(self, fromID, toID, dedication):
        fromU = await self.getUser(fromID)
        toU = await self.getUser(toID)

        if not dedication:
            await toU.send(":partying_face: {} wishes you a nice day! :partying_face:".format(fromU.mention))
        else:
            await toU.send("{} has a message for you: {}".format(fromU.mention, dedication))  

    def enviarMSG(self, fromID, toID, dedication):
        asyncio.run_coroutine_threadsafe(self.sendAsync(fromID, toID, dedication), self.loopprinc)

    async def on_ready(self):
        print("Bot iniciado como {}".format(self.user))

