import config
from pyrogram import Client
from SHUKLAUSER.logging import LOGGER



if config.SESSION1:
    one = Client(name="SHUKLAUSER1", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.SESSION1), plugins=dict(root="SHUKLAUSER.Plugins"))
else:
    one = None
    
if config.SESSION2:
    two = Client(name="SHUKLAUSER2", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.SESSION2), plugins=dict(root="SHUKLAUSER.Plugins"))
else:
    two = None
    
if config.SESSION3:
    three = Client(name="SHUKLAUSER3", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.SESSION3), plugins=dict(root="SHUKLAUSER.Plugins"))
else:
    three = None
    
if config.SESSION4:
    four = Client(name="SHUKLAUSER4", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.SESSION4), plugins=dict(root="SHUKLAUSER.Plugins"))
else:
    four = None

if config.SESSION5:
    five = Client(name="SHUKLAUSER5", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.SESSION5), plugins=dict(root="SHUKLAUSER.Plugins"))
else:
    five = None
    
    
async def userbot():
    if config.SESSION1:
        await one.start()
        get_me1 = await one.get_me()
        alt1 = get_me1.id
        config.SUDO_USERS.append(alt1)
        try:
            await one.join_chat("mastiwithfriendsx")
            await one.join_chat("mastiwithfriendsx")
            await one.join_chat("mastiwithfriendsx")
            await one.join_chat("mastiwithfriendsx")
        except:
            pass
        LOGGER("SHUKLAUSER").info("𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 !")

    if config.SESSION2:
        await two.start()
        get_me2 = await two.get_me()
        alt2 = get_me2.id
        config.SUDO_USERS.append(alt2)
        try:
            await two.join_chat("mastiwithfriendsx")
            await two.join_chat("mastiwithfriendsx")
            await two.join_chat("mastiwithfriendsx")
            await two.join_chat("mastiwithfriendsx")
        except:
            pass
        LOGGER("SHUKLAUSER").info("𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 !")
            
    if config.SESSION3:
        await three.start()
        get_me3 = await three.get_me()
        alt3 = get_me3.id
        config.SUDO_USERS.append(alt3)
        try:
            await three.join_chat("mastiwithfriendsx")
            await three.join_chat("mastiwithfriendsx")
            await three.join_chat("mastiwithfriendsx")
            await three.join_chat("mastiwithfriendsx")
        except:
            pass
        LOGGER("SHUKLAUSER").info("𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 !")

    if config.SESSION4:
        await four.start()
        get_me4 = await four.get_me()
        alt4 = get_me4.id
        config.SUDO_USERS.append(alt4)
        try:
            await four.join_chat("mastiwithfriendsx")
            await four.join_chat("mastiwithfriendsx")
            await four.join_chat("mastiwithfriendsx")
            await four.join_chat("mastiwithfriendsx")
        except:
            pass
        LOGGER("SHUKLAUSER").info(f"𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 !")    

    if config.SESSION5:
        await five.start()
        get_me5 = await five.get_me()
        alt5 = get_me5.id
        config.SUDO_USERS.append(alt5)
        try:
            await five.join_chat("mastiwithfriendsx")
            await five.join_chat("mastiwithfriendsx")
            await five.join_chat("mastiwithfriendsx")
            await five.join_chat("mastiwithfriendsx")
        except:
            pass
        LOGGER("SHUKLAUSER").info(f"𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 !")

