import os
import math
import asyncio
import shutil
import socket
import dotenv
import heroku3
import urllib3
import requests
import config
from git import Repo
from os import remove
from pyrogram import filters, Client
from pyrogram.types import Message
from datetime import datetime
from config import OWNER_ID
from SHUKLAUSER import app
from SHUKLAUSER.misc import HAPP, XCB
from SHUKLAUSER.Helpers import Pastebin
from git.exc import GitCommandError, InvalidGitRepositoryError


__NAME__ = "Oᴡɴᴇʀ"
__HELP__ = """
⊱ `usage` : sʜᴏᴡs ᴛʜᴇ ᴅʏɴᴏ ᴜsᴀɢᴇ ᴏғ ᴛʜᴇ ᴍᴏɴᴛʜ.

⊱ `getvar [ᴠᴀʀ ɴᴀᴍᴇ] [ᴠᴀʟᴜᴇ]` : ɢᴇᴛ ᴀ ᴄᴏɴғɪɢ ᴠᴀʀ ғʀᴏᴍ ʜᴇʀᴏᴋᴜ ᴏʀ .ᴇɴᴠ

⊱ `delvar [ᴠᴀʀ ɴᴀᴍᴇ] [ᴠᴀʟᴜᴇ]` : ᴅᴇʟᴇᴛᴇ ᴀ ᴄᴏɴғɪɢ ᴠᴀʀ ᴏɴ ʜᴇʀᴏᴋᴜ ᴏʀ .ᴇɴᴠ

⊱ `setvar [ᴠᴀʀ ɴᴀᴍᴇ] [ᴠᴀʟᴜᴇ]` : sᴇᴛ ᴏʀ ᴜᴩᴅᴀᴛᴇ ᴀ ᴄᴏɴғɪɢ ᴠᴀʀ ᴏɴ ʜᴇʀᴏᴋᴜ ᴏʀ .ᴇɴᴠ

⊱ `reboot` : ʀᴇʙᴏᴏᴛ ʏᴏᴜʀ ʙᴏᴛ

⊱ `update` : ᴜᴩᴅᴀᴛᴇ ᴛʜᴇ ʙᴏᴛ ғʀᴏᴍ ᴛʜᴇ ᴜᴩsᴛʀᴇᴀᴍ ʀᴇᴩᴏ

⊱ `logs` : ɢᴇᴛ ʟᴏɢs ᴏғ ʏᴏᴜʀ ʙᴏᴛ 
"""


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def is_heroku():
    return "heroku" in socket.getfqdn()


@Client.on_message(filters.command(["logs", "getlog", "log"], ["/", ".", "!"]) & filters.user(OWNER_ID))
async def log_(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text("ᴘʟᴇᴀsᴇ ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜʀ **ʜᴇʀᴏᴋᴜ ᴀᴘɪ ᴋᴇʏ** ᴀɴᴅ **ʜᴇʀᴏᴋᴜ ᴀᴘᴘ ɴᴀᴍᴇ** ᴀʀᴇ ᴄᴏɴꜰɪɢᴜʀᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ʜᴇʀᴏᴋᴜ")
        data = HAPP.get_log()
        link = await Pastebin(data)
        if link:
            return await message.reply_text(link)
        else:
            ran_hash = "logs.txt"
            with open(ran_hash, "w") as lyr:
                lyr.write(data)
            try:
                await message.reply_document(ran_hash)
            except Exception as e:
                await message.reply_text("ᴀɴ ᴇxᴄᴇᴘᴛɪᴏɴ ᴏᴄᴄᴜʀᴇᴅ !\n\n{0}".format(str(e)))
            finally:
                remove(ran_hash)
    else:
        if os.path.exists("logs.txt"):
            log = open("logs.txt")
            lines = log.readlines()
            data = ""
            try:
                NUMB = int(message.text.split(None, 1)[1])
            except:
                NUMB = 100
            for x in lines[-NUMB:]:
                data += x
            link = await Pastebin(data)
            if link:
                return await message.reply_text(link)
            else:
                await message.reply_document("logs.txt")
        else:
            return await message.reply_text("ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ɢᴇᴛ ʟᴏɢs ᴏꜰ ʜᴇʀᴏᴋᴜ ᴀᴘᴘs.")


@Client.on_message(filters.command(["getvar"], ["/", ".", "!"]) & filters.user(OWNER_ID) & ~filters.forwarded)
async def varget_(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    usage = "**ᴜsᴀɢᴇ:**\n/getvar [ᴠᴀʀ-ɴᴀᴍᴇ]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text("ᴘʟᴇᴀsᴇ ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜʀ **ʜᴇʀᴏᴋᴜ ᴀᴘɪ ᴋᴇʏ** ᴀɴᴅ **ʜᴇʀᴏᴋᴜ ᴀᴘᴘ ɴᴀᴍᴇ** ᴀʀᴇ ᴄᴏɴꜰɪɢᴜʀᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ʜᴇʀᴏᴋᴜ")
        heroku_config = HAPP.config()
        if check_var in heroku_config:
            return await message.reply_text(f"**{check_var}:** `{heroku_config[check_var]}`")
        else:
            return await message.reply_text("ᴜɴᴀʙʟᴇ ᴛᴏ ꜰɪɴᴅ ᴀɴʏ sᴜᴄʜ ᴠᴀʀ.")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".ᴇɴᴠ ꜰɪʟᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ.")
        output = dotenv.get_key(path, check_var)
        if not output:
            await message.reply_text("ᴜɴᴀʙʟᴇ ᴛᴏ ꜰɪɴᴅ ᴀɴʏ sᴜᴄʜ ᴠᴀʀ.")
        else:
            return await message.reply_text(f"**{check_var}:** `{str(output)}`")


@Client.on_message(filters.command(["delvar"], ["/", ".", "!"]) & filters.user(OWNER_ID) & ~filters.forwarded)
async def vardel_(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    usage = "**ᴜsᴀɢᴇ:**\n/delvar [ᴠᴀʀ-ɴᴀᴍᴇ]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text("ᴘʟᴇᴀsᴇ ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜʀ **ʜᴇʀᴏᴋᴜ ᴀᴘɪ ᴋᴇʏ** ᴀɴᴅ **ʜᴇʀᴏᴋᴜ ᴀᴘᴘ ɴᴀᴍᴇ** ᴀʀᴇ ᴄᴏɴꜰɪɢᴜʀᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ʜᴇʀᴏᴋᴜ")
        heroku_config = HAPP.config()
        if check_var in heroku_config:
            await message.reply_text("{0} ᴅᴇʟᴇᴛᴇᴅ.".format(check_var))
            del heroku_config[check_var]
        else:
            return await message.reply_text("ᴜɴᴀʙʟᴇ ᴛᴏ ꜰɪɴᴅ ᴀɴʏ sᴜᴄʜ ᴠᴀʀ.")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".ᴇɴᴠ ꜰɪʟᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ.")
        output = dotenv.unset_key(path, check_var)
        if not output[0]:
            return await message.reply_text("ᴜɴᴀʙʟᴇ ᴛᴏ ꜰɪɴᴅ ᴀɴʏ sᴜᴄʜ ᴠᴀʀ.")
        else:
            await message.reply_text("{0} ᴅᴇʟᴇᴛᴇᴅ.".format(check_var))
            os.system(f"kill -9 {os.getpid()} && python3 -m SHUKLAUSER")


@Client.on_message(filters.command(["setvar"], ["/", ".", "!"]) & filters.user(OWNER_ID) & ~filters.forwarded)
async def set_var(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    usage = "**ᴜsᴀɢᴇ:**\n/setvar [ᴠᴀʀ-ɴᴀᴍᴇ] [ᴠᴀʀ-ᴠᴀʟᴜᴇ]"
    if len(message.command) < 3:
        return await message.reply_text(usage)
    to_set = message.text.split(None, 2)[1].strip()
    value = message.text.split(None, 2)[2].strip()
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text("ᴘʟᴇᴀsᴇ ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜʀ **ʜᴇʀᴏᴋᴜ ᴀᴘɪ ᴋᴇʏ** ᴀɴᴅ **ʜᴇʀᴏᴋᴜ ᴀᴘᴘ ɴᴀᴍᴇ** ᴀʀᴇ ᴄᴏɴꜰɪɢᴜʀᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ʜᴇʀᴏᴋᴜ")
        heroku_config = HAPP.config()
        if to_set in heroku_config:
            await message.reply_text("{0} ʜᴀs ʙᴇᴇɴ ᴜᴘᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ.".format(to_set))
        else:
            await message.reply_text("{0} ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ.".format(to_set))
        heroku_config[to_set] = value
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".ᴇɴᴠ ꜰɪʟᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ.")
        dotenv.set_key(path, to_set, value)
        if dotenv.get_key(path, to_set):
            await message.reply_text("{0} ʜᴀs ʙᴇᴇɴ ᴜᴘᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ.".format(to_set))
        else:
            await message.reply_text("{0} ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ.".format(to_set))
        os.system(f"kill -9 {os.getpid()} && python3 -m SHUKLAUSER")


@Client.on_message(filters.command(["usage"], ["/", ".", "!"]) & filters.user(OWNER_ID) & ~filters.forwarded)
async def usage_dynos(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text("ᴘʟᴇᴀsᴇ ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜʀ **ʜᴇʀᴏᴋᴜ ᴀᴘɪ ᴋᴇʏ** ᴀɴᴅ **ʜᴇʀᴏᴋᴜ ᴀᴘᴘ ɴᴀᴍᴇ** ᴀʀᴇ ᴄᴏɴꜰɪɢᴜʀᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ʜᴇʀᴏᴋᴜ")
    else:
        return await message.reply_text("ᴏɴʟʏ ꜰᴏʀ ʜᴇʀᴏᴋᴜ ᴀᴘᴘs .")
    dyno = await message.reply_text("ᴄʜᴇᴄᴋɪɴɢ ʜᴇʀᴏᴋᴜ ᴜsᴀɢᴇ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ!")
    Heroku = heroku3.from_key(config.HEROKU_API_KEY)
    account_id = Heroku.account().id
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {config.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + account_id + "/actions/get-quota"
    r = requests.get("https://api.heroku.com" + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("Unable to fetch.")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    text = f"""
**ʜᴇʀᴏᴋᴜ ᴅʏɴᴏs ᴜsᴀɢᴇ**

<u>ᴜsᴀɢᴇ:</u>
ᴛᴏᴛᴀʟ ᴜsᴇᴅ: `{AppHours}`**ʜ**  `{AppMinutes}`**ᴍ**  [`{AppPercentage}`**%**]

<u>ʀᴇᴍᴀɪɴɪɴɢ ᴅʏɴᴏs:</u>
ᴛᴏᴛᴀʟ ʟᴇғᴛ: `{hours}`**ʜ**  `{minutes}`**ᴍ**  [`{percentage}`**%**]"""
    return await dyno.edit(text)


@Client.on_message(filters.command(["update", "gitpull"], ["/", ".", "!"]) & filters.user(OWNER_ID) & ~filters.forwarded)
async def update_(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text("ᴘʟᴇᴀsᴇ ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜʀ **ʜᴇʀᴏᴋᴜ ᴀᴘɪ ᴋᴇʏ** ᴀɴᴅ **ʜᴇʀᴏᴋᴜ ᴀᴘᴘ ɴᴀᴍᴇ** ᴀʀᴇ ᴄᴏɴꜰɪɢᴜʀᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ ɪɴ ʜᴇʀᴏᴋᴜ")
    response = await message.reply_text("ᴄʜᴇᴄᴋɪɴɢ ꜰᴏʀ ᴀᴠᴀɪʟᴀʙʟᴇ ᴜᴘᴅᴀᴛᴇs ")
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit("ɢɪᴛ ᴄᴏᴍᴍᴀɴᴅ ᴇʀʀᴏʀ")
    except InvalidGitRepositoryError:
        return await response.edit("ɪɴᴠᴀʟɪᴅ ɢɪᴛ ʀᴇᴘosɪᴛᴏʀʏ")
    to_exc = f"git fetch origin {config.UPSTREAM_BRANCH} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]  # main git repository

    for checks in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit("ʙᴏᴛ ɪs ᴜᴩ-ᴛᴏ-ᴅᴀᴛᴇ ᴡɪᴛʜ ᴜᴩsᴛʀᴇᴀᴍ ʀᴇᴩᴏ !")
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[
            (format // 10 % 10 != 1)
            * (format % 10 < 4)
            * format
            % 10 :: 4
        ],
    )
    for info in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        updates += f"<b>➣ #{info.count()}: [{info.summary}]({REPO_}/commit/{info}) by -> {info.author}</b>\n\t\t\t\t<b>➥ ᴄᴏᴍᴍɪᴛᴇᴅ ᴏɴ:</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    
    _update_response_ = "<b>ᴀ ɴᴇᴡ ᴜᴩᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ !</b>\n\n➣ ᴩᴜsʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ɴᴏᴡ</code>\n\n**<u>ᴜᴩᴅᴀᴛᴇs:</u>**\n\n"
    _final_updates_ = _update_response_ + updates

    if len(_final_updates_) > 4096:
        url = await Pastebin(updates)
        nrs = await response.edit(
            f"<b>ᴀ ɴᴇᴡ ᴜᴩᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ !</b>\n\n➣ ᴩᴜsʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ɴᴏᴡ</code>\n\n**<u>ᴜᴩᴅᴀᴛᴇs:</u>**\n\n[ᴄʜᴇᴄᴋ ᴜᴩᴅᴀᴛᴇs]({url})"
        )
    else:
        nrs = await response.edit(_final_updates_, disable_web_page_preview=True)

    os.system("git stash &> /dev/null && git pull")

    if await is_heroku():
        try:
            await response.edit(f"{nrs.text}\n\nʙᴏᴛ ᴜᴩᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ! ɴᴏᴡ ᴡᴀɪᴛ ғᴏʀ ғᴇᴡ ᴍɪɴᴜᴛᴇs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴛᴀʀᴛs ᴀɴᴅ ᴩᴜsʜ ᴄʜᴀɴɢᴇs !")
            os.system(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
        except Exception as err:
            await response.edit(f"{nrs.text}\n\nsᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴡʜᴇɴ ᴛʀɪᴇᴅ ᴛᴏ ʀᴇsᴛᴀʀᴛ")
            print(err)
            return
    else:
        await response.edit(f"{nrs.text}\n\nʙᴏᴛ ᴜᴩᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ! ɴᴏᴡ ᴡᴀɪᴛ ғᴏʀ ғᴇᴡ ᴍɪɴᴜᴛᴇs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴛᴀʀᴛs ᴀɴᴅ ᴩᴜsʜ ᴄʜᴀɴɢᴇs !")
        os.system("pip3 install -r requirements.txt")
        os.system(f"kill -9 {os.getpid()} && python3 -m SHUKLAUSER")
        exit()


@Client.on_message(filters.command(["reboot"], ["/", ".", "!"]) & filters.user(OWNER_ID) & ~filters.forwarded)
async def reboot_(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    response = await message.reply_text("ʀᴇsᴛᴀʀᴛɪɴɢ...")
    try:
        shutil.rmtree("downloads")
        shutil.rmtree("raw_files")
        shutil.rmtree("cache")
    except:
        pass
    await response.edit_text("ʀᴇsᴛᴀʀᴛ ᴩʀᴏᴄᴇss sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ, ᴡᴀɪᴛ ғᴏʀ ғᴇᴡ ᴍɪɴᴜᴛᴇs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴛᴀʀᴛs.")
    os.system(f"kill -9 {os.getpid()} && python3 -m SHUKLAUSER")
