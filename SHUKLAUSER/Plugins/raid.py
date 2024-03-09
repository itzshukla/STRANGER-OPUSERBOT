# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑻𝒆𝒂𝒎 𝑺𝒕𝒓𝒂𝒏𝒈𝒆𝒓
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅

import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from data import THE_SHUKLA, RAID
from config import OWNER_ID, SUDO_USERS



__NAME__ = "Rᴀɪᴅ"
__HELP__ = """
⊱ `raid` : ʀᴀɪᴅ ᴏɴ ᴀɴʏ ᴜsᴇʀ

⊱ `rraid` : ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ᴜsᴇʀ

⊱ `draid` : ᴅᴇʟᴇᴛᴇ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ᴜsᴇʀ
"""


WWW = []


@Client.on_message(filters.command(["raid"], ["/", "!", "."]) & filters.user(SUDO_USERS))
async def raid(xspam: Client, message: Message):
      alt = message.text.split(" ")
      if len(alt) > 2:
            ok = await xspam.get_users(alt[2])
            id = ok.id
            if id in THE_SHUKLA:
                  await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ  ᴏᴡɴᴇʀ !")
            elif id == OWNER_ID:
                  await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛꜱ !")
            elif id in SUDO_USERS:
                  await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !")
            else:
                  counts = int(alt[1])
                  fname = ok.first_name
                  mention = f"[{fname}](tg://user?id={id})"
                  for _ in range(counts):
                        reply = choice(RAID)
                        msg = f"{mention} {reply}"
                        await xspam.send_message(message.chat.id, msg)
                        await asyncio.sleep(0.3)

      elif message.reply_to_message and (len(alt) == 2):
            user_id = message.reply_to_message.from_user.id
            ok = await xspam.get_users(user_id)
            id = ok.id
            if id in THE_SHUKLA:
                  await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ  ᴏᴡɴᴇʀ !")
            elif id == OWNER_ID:
                  await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛꜱ !")
            elif id in SUDO_USERS:
                  await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !")
            else:
                  counts = int(alt[1])
                  fname = ok.first_name
                  mention = f"[{fname}](tg://user?id={id})"
                  for _ in range(counts):
                        reply = choice(RAID)
                        msg = f"{mention} {reply}"
                        await xspam.send_message(message.chat.id, msg)
                        await asyncio.sleep(0.3)

      else:
          await message.reply_text("⚡ ᴜsᴀɢᴇ:\n\n» !raid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n» !raid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@Client.on_message(filters.command(["rraid", "replyraid"], ["/", ".", "!"]) & filters.user(SUDO_USERS))
async def rraid(xspam: Client, message: Message):
      global WWW
      alt = message.text.split(" ")
      if len(alt) > 1:
          ok = await xspam.get_users(alt[1])
          id = ok.id
          if id in THE_SHUKLA:
                await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ  ᴏᴡɴᴇʀ !")
          elif id == OWNER_ID:
                await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛꜱ !")
          elif id in SUDO_USERS:
                await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !")
          else:
              WWW.append(id)
              await message.reply_text("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ !! ✅")

      elif message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
          if user_id in THE_SHUKLA:
                await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ  ᴏᴡɴᴇʀ !")
          elif user_id == OWNER_ID:
                await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇ ʙᴏᴛꜱ !")
          elif user_id in SUDO_USERS:
                await message.reply_text("» ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !")
          else:
              WWW.append(user_id)
              await message.reply_text("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ !! ✅")

      else:
          await message.reply_text("⚡ ᴜsᴀɢᴇ:\n\n» !rraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n» !rraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@Client.on_message(filters.command(["drraid", "draid", "dreplyraid"], ["/", ".", "!"]) & filters.user(SUDO_USERS))
async def draid(xspam: Client, message: Message):
      global WWW
      alt = message.text.split(" ")
      if len(alt) > 1:
          ok = await xspam.get_users(alt[1])
          id = ok.id
          if id in WWW:
              WWW.remove(id)
              await message.reply_text("» ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ !! ✅")

      elif message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if id in WWW:
              WWW.remove(id)
              await message.reply_text("» ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ !! ✅")

      else:
          await message.reply_text("⚡ ᴜsᴀɢᴇ:\n\n» !draid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n» !draid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
    

@Client.on_message(~filters.me & filters.incoming)
async def watcher(_, msg: Message):
      global WWW
      id = msg.from_user.id
      if id in WWW:
            reply = choice(RAID)
            await msg.reply_text(reply)
