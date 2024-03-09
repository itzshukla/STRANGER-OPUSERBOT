# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑻𝒆𝒂𝒎 𝑺𝒕𝒓𝒂𝒏𝒈𝒆𝒓
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅

import re
import traceback
from SHUKLAUSER import app, one, two, __Version__
from SHUKLAUSER.Helpers import page_load, inline_wrapper
from config import HELPABLE, SUDO_USERS, EXTRA_IMG
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import ChatWriteForbidden, UserBannedInChannel
from pyrogram.types import Message, InputTextMessageContent, InlineQueryResultPhoto, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery
from sys import version as pyver


__NAME__ = "Hᴇʟᴘ"
__HELP__ = """
⊱ `help` : ɢᴇᴛ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ᴜsᴇʀʙᴏᴛ ᴀɴᴅ ʙᴏᴛ
"""


def private_panel():
    buttons = [
        [
            InlineKeyboardButton(text="Uᴘᴅᴀᴛᴇꜱ", url="https://t.me/SHIVANSH474"),
        ],
        [
            InlineKeyboardButton(text="Hᴇʟᴘ Mᴇɴᴜ", callback_data="home_help"),
        ]
    ]
    return buttons


TXT = f"ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ !" 

QA = "ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ sᴛʀᴀɴɢᴇʀ sᴘᴀᴍ ᴜsᴇʀʙᴏᴛ \n\n\nᴄᴏᴘʏʀɪɢʜᴛ ʙʏ @mastiwithfriendsx\nᴄᴏᴅᴇ ʙʏ @SHIVANSH39"

HMH = f"""
™°‌ 𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 sᴘᴀᴍ ᴠᴇʀsɪᴏɴ : `{__Version__}`
ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : `{pyver.split()[0]}`
ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : `{pyrover}`

**ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.**"""


@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(_, query: CallbackQuery):
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
  
    if mod_match:
        try:
            module = mod_match.group(1)
            text = (
                "{} **--{}--** :\n\n".format("Aʟʟ Cᴏᴍᴍᴀɴᴅs Cᴀɴ Bᴇ Usᴇᴅ Wɪᴛʜ : `[/,  !,  .]`\n\nHᴇʟᴘ Fᴏʀ", HELPABLE[module].__NAME__)
                + HELPABLE[module].__HELP__
            )
            key = InlineKeyboardMarkup([[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="back")]])
            try:
                await query.message.edit(text=text, reply_markup=key)
            except:
                if query.from_user.id in SUDO_USERS:
                    await app.edit_inline_text(query.inline_message_id, text=text, reply_markup=key)
                else:
                    await query.answer(text=QA, show_alert=True)
        except:
            return
        
    elif prev_match:
        try:
            current_page = int(prev_match.group(1))
            buttons = InlineKeyboardMarkup(page_load(current_page - 1, HELPABLE, "help"))
            try:
                await query.message.edit(text=TXT, reply_markup=buttons)
            except:
                if query.from_user.id in SUDO_USERS:
                    await app.edit_inline_text(query.inline_message_id, text=TXT, reply_markup=buttons)
                else:
                    await query.answer(text=QA, show_alert=True)
        except:
            return
        
    elif next_match:
        try:
            current_page = int(next_match.group(1))
            buttons = InlineKeyboardMarkup(page_load(current_page + 1, HELPABLE, "help"))
            try:
                await query.message.edit(text=TXT, reply_markup=buttons)
            except:
                if query.from_user.id in SUDO_USERS:
                    await app.edit_inline_text(query.inline_message_id, text=TXT, reply_markup=buttons)
                else:
                    await query.answer(text=QA, show_alert=True)
        except:
            return
       

@app.on_callback_query(filters.regex("home_help"))
async def back(_, query: CallbackQuery):
    try:
        buttons = InlineKeyboardMarkup(page_load(0, HELPABLE, "help"))
        try:
            await query.message.edit(text=TXT, reply_markup=buttons)
        except:
            if query.from_user.id in SUDO_USERS:
                await app.edit_inline_text(query.inline_message_id, text=TXT, reply_markup=buttons)
            else:
                await query.answer(text=QA, show_alert=True)
    except:
        return


@app.on_callback_query(filters.regex("back"))
async def back(_, query: CallbackQuery):
    try:
        buttons = InlineKeyboardMarkup(page_load(0, HELPABLE, "help"))
        try:
            await query.message.edit(text=TXT, reply_markup=buttons)
        except:
            if query.from_user.id in SUDO_USERS:
                await app.edit_inline_text(query.inline_message_id, text=TXT, reply_markup=buttons)
            else:
                await query.answer(text=QA, show_alert=True)
    except:
        return
    
    
@app.on_callback_query(filters.regex("semxx"))
async def back(_, query: CallbackQuery):
    try:
        buttons = InlineKeyboardMarkup(private_panel())
        try:
            await query.message.edit(text=HMH, reply_markup=buttons)
        except:
            if query.from_user.id in SUDO_USERS:
                await app.edit_inline_text(query.inline_message_id, text=HMH, reply_markup=buttons)
            else:
                await query.answer(text=QA, show_alert=True)
    except:
        return


async def help_function(answers):
    bttn = page_load(0, HELPABLE, "help")
    answers.append(
        InlineQueryResultPhoto(
            photo_url=EXTRA_IMG,
            thumb_url=EXTRA_IMG,
            title="HELP MENU",
            caption=HMH,
            reply_markup=InlineKeyboardMarkup(bttn),
            input_message_content=InputTextMessageContent(message_text=HMH)
        )
    )
    return answers


@app.on_inline_query()
@inline_wrapper
async def inline_query_handler(bot: app, query: InlineQuery):
    try:
        alpha = query.query.lower()
        answer = []
        answer = await help_function(answer)
        await bot.answer_inline_query(query.id, results=answer)
    except Exception as e:
        e = traceback.format_exc()
        print(e, "InLine")


@Client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.user(SUDO_USERS))
async def func_help(_, message: Message):
    chat = message.chat.id
    alt = message.text.split()[0]
    if alt:
        try:
            if one:
                hero = await one.get_inline_bot_results(bot=f"@{app.username}", query="help")
                await one.send_inline_bot_result(chat, hero.query_id, hero.results[0].id)
            else:
                hero = await two.get_inline_bot_results(bot=f"@{app.username}", query="help")
                await two.send_inline_bot_result(chat, hero.query_id, hero.results[0].id)
        except (ChatWriteForbidden, UserBannedInChannel):
            print("ID is limited OR muted in the chat")
            return
        except Exception as e:
            await message.reply_text(f"Inline Help Menu Not Supported In This Chat Go To Bot's Dm For Help Menu @{app.username}")
            print(e)



@app.on_message(filters.command(["start", "help"]) & filters.private)
async def start_cmd(_, msg: Message):
    try:
        await msg.delete()
    except:
        pass
    buttons = InlineKeyboardMarkup(page_load(0, HELPABLE, "help"))
    await msg.reply_photo(
        photo=EXTRA_IMG,
        caption=HMH,
        reply_markup=buttons
    )
    
