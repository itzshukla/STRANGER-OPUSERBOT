# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑻𝒆𝒂𝒎 𝑺𝒕𝒓𝒂𝒏𝒈𝒆𝒓
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅

import datetime
from sys import version as pyver
from config import EXTRA_IMG, SUDO_USERS
from SHUKLAUSER import __Version__, app
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.types import Message


__NAME__ = "Aʟɪᴠᴇ"
__HELP__ = """
⊱ `ping` : ɢᴇᴛ ᴘɪɴɢ ᴏғ ᴜsᴇʀʙᴏᴛ

⊱ `alive` : ɢᴇᴛ ᴀʟɪᴠᴇ ᴍᴇssᴀɢᴇ ᴏғ ᴜsᴇʀʙᴏᴛ ᴀɴᴅ ʙᴏᴛ ᴛᴏᴏ

⊱ `start` : sᴛᴀʀᴛ ᴄᴍᴅ ғᴏʀ ʙᴏᴛ
"""


ALT = f"""
™°‌ 𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 ᴠᴇʀsɪᴏɴ : `{__Version__}`
➪𝗣ʏᴛʜᴏɴ 𝗩ᴇʀsɪᴏɴ : `{pyver.split()[0]}`
➪𝗣ʏʀᴏɢʀᴀᴍ 𝗩ᴇʀsɪᴏɴ : `{pyrover}`
➪𝗨ᴘᴅᴀᴛᴇꜱ : @itszShukla\n"""


@Client.on_message(filters.command(["ping"], ["/", ".", "!"]) & filters.user(SUDO_USERS))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"◇ ᴛʜᴇ ™°‌ 𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑\n◇ ᴘɪɴɢ: `{ms}ms`\n◇ ᴠᴇʀsɪᴏɴ: `{__Version__}`")


@app.on_message(filters.command(["alive"], ["/", ".", "!"]) & filters.user(SUDO_USERS))
@Client.on_message(filters.command(["alive"], ["/", ".", "!"]) & filters.user(SUDO_USERS))
async def alive(xspam: Client, msg: Message):
       if ".jpg" in EXTRA_IMG or ".png" in EXTRA_IMG:
              await xspam.send_photo(msg.chat.id, EXTRA_IMG, caption=ALT)
       if ".mp4" in EXTRA_IMG or ".mp4" in EXTRA_IMG:
              await xspam.send_video(msg.chat.id, EXTRA_IMG, caption=ALT)

