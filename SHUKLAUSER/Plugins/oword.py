# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑻𝒆𝒂𝒎 𝑺𝒕𝒓𝒂𝒏𝒈𝒆𝒓
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅

import os
import asyncio
from pyrogram.types import Message
from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from config import SUDO_USERS
from data import OneWord


__NAME__ = "Oᴡᴏʀᴅ"
__HELP__ = """
ᴛʜɪs ɪs ᴀ ғᴇᴀᴛᴜʀᴇ ɪɴ ᴡʜɪᴄʜ ᴜsᴇʀʙᴏᴛ sᴇɴᴅs ᴏɴᴇ ᴡᴏʀᴅ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ʜᴀs sᴘᴇᴄɪᴀʟ ᴄᴏᴍᴍᴀɴᴅ 


sʟᴏᴡ ᴏɴᴇ ᴡᴏʀᴅ ⊱ `[l0l, madarchod, randi]`

ғᴀsᴛ ᴏɴᴇ ᴡᴏʀᴅ ⊱ `[fword, lund, behenchod, gay]`
"""

FC = 2

@Client.on_message(filters.command(["randi", "l0l", "madarchod"], ["", ".", "!", "/"]) & filters.user(SUDO_USERS), group=FC)
async def alt_lol(xspam: Client, message: Message):    
    chat_id = message.chat.id
    RUSH = None
    if message.reply_to_message:
        RUSH = message.reply_to_message.id
    try:
        for word in OneWord:
            await xspam.send_message(chat_id, word, reply_to_message_id=RUSH)
            await asyncio.sleep(1)
    except FloodWait:
        print("Flood !!")
        pass


@Client.on_message(filters.command(["gay", "fword", "behenchod", "lund"], ["", ".", "!", "/"]) & filters.user(SUDO_USERS), group=FC)
async def alt_mkc(xspam: Client, message: Message):    
    chat_id = message.chat.id
    RUSH = None
    if message.reply_to_message:
        RUSH = message.reply_to_message.id
    try:
        for word in OneWord:
            await xspam.send_message(chat_id, word, reply_to_message_id=RUSH)
            await asyncio.sleep(000.1)
    except FloodWait:
        print("Flood !!")
        pass
    
    
@Client.on_message(filters.command(["stop"], ["", ".", "!", "/"]) & filters.user(SUDO_USERS), group=FC)
async def alt_stop(_, message: Message):    
    reply = await message.reply_text("sᴛᴏᴘᴘɪɴɢ ...")
    await reply.edit("sᴛᴏᴘᴘᴇᴅ !!\n\nᴡᴀɪᴛ ғᴏʀ 2 ᴍɪɴᴜᴛᴇs !!")
    os.system(f"kill -9 {os.getpid()} && python3 -m SHUKLAUSER")
    
    
