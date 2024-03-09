from config import API_ID, API_HASH, BOT_TOKEN
from pyrogram import Client
from SHUKLAUSER.logging import LOGGER


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="SHUKLAUSER",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            in_memory=True
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        if get_me.last_name:
            self.name = get_me.first_name + "" + get_me.last_name
        else:
            self.name = get_me.last_name
        self.username = get_me.username
        self.mention = get_me.mention
        self.id = get_me.id
        LOGGER("SHUKLAUSER").info(f"Started As {self.name} !")

    async def stop(self):
        await super().stop()
        

app = Bot()