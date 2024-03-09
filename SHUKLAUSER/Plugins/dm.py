# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑻𝒆𝒂𝒎 𝑺𝒕𝒓𝒂𝒏𝒈𝒆𝒓
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅

import asyncio
from random import choice
from pyrogram import filters, Client
from pyrogram.types import Message
from data import RAID, THE_SHUKLA
from config import SUDO_USERS


__NAME__ = "Dᴍ"
__HELP__ = """
⊱ `dmraid` : ʀᴀɪᴅ ɪɴ ᴅᴍ ᴏғ ᴀɴʏ ᴜsᴇʀ

⊱ `dmspam` : sᴘᴀᴍ ɪɴ ᴅᴍ ᴏғ ᴀɴʏ ᴜsᴇʀ
"""


@Client.on_message(filters.command(["dmraid"], [".", "/", "!"]) & filters.user(SUDO_USERS))
async def dmraid(xspam: Client, message: Message):
      alt = message.text.split(" ")
      if len(alt) == 3:
          ok = await xspam.get_users(alt[2])
          id = ok.id
          if id in THE_SHUKLA:
                await message.reply_text(f"ᴠᴇʀɪғɪᴇᴅ ʙʏ ™°‌ 𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 !")
          elif id in SUDO_USERS:
                await message.reply_text(f"ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ !")
          else:
              counts = int(alt[1])
              await message.reply_text("ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ !")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.1)

      elif message.reply_to_message and (len(alt) == 2):
          user_id = message.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if id in THE_SHUKLA:
                await message.reply_text(f"ᴠᴇʀɪғɪᴇᴅ ™°‌ 𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 !")
          elif id in SUDO_USERS:
                await message.reply_text(f"ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ !")
          else:
              counts = int(alt[1])
              await message.reply_text("ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ !")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.1)
                    
      else:
            await message.reply_text("⚡ ᴜsᴀɢᴇ:\n\n!dmraid 13 <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ>")


@Client.on_message(filters.command(["dmspam"], [".", "!", "/"]) & filters.user(SUDO_USERS))
async def dmspam(xspam: Client, message: Message):
    alt = message.text.split(" ", 3)
    if  len(alt) == 4:
        uid = int(alt[2])
        if uid in THE_SHUKLA:
            await message.reply_text(f"ᴠᴇʀɪғɪᴇᴅ ʙʏ ™°‌ 𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 !")
        elif uid in SUDO_USERS:
            await message.reply_text(f"ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ !")
        else:
            quantity, spam_text = int(alt[1]), alt[3]
            await message.reply_text("ᴅᴍ ꜱᴘᴀᴍ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ !")
            for _ in range(quantity):
                await xspam.send_message(uid, spam_text)
                await asyncio.sleep(0.3)

    elif message.reply_to_message and (len(alt) == 3):
        id = message.reply_to_message.from_user.id
        if id in THE_SHUKLA:
            await message.reply_text(f"™°‌ 𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 !")
        elif id in SUDO_USERS:
            await message.reply_text(f"ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ !")
        else:
            quantity = int(alt[1])
            spam_text = alt[2]
            await message.reply_text("ᴅᴍ ꜱᴘᴀᴍ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ !")
            for _ in range(quantity):
                await xspam.send_message(id, spam_text)
                await asyncio.sleep(0.3)

    else:
        await message.reply_text("⚡ ᴜsᴀɢᴇ:\n\n!dmspam 13 <ᴜꜱᴇʀ ɪᴅ> sᴛʀᴀɴɢᴇʀ\n\n !dmspam 13 shivansh papa <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>")
