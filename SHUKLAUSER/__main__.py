import asyncio
import importlib
from pyrogram import idle
from SHUKLAUSER import app
from config import HELPABLE
from SHUKLAUSER.Plugins import ALL_MODULES
from SHUKLAUSER.logging import LOGGER
from SHUKLAUSER.Helpers import userbot, one, two


loop = asyncio.get_event_loop()


async def init(): 
    await app.start()

    for all_module in ALL_MODULES:
        imported_module = importlib.import_module("SHUKLAUSER.Plugins." + all_module)
        
        if (hasattr(imported_module, "__NAME__") and imported_module.__NAME__):
            imported_module.__NAME__ = imported_module.__NAME__
            
            if (hasattr(imported_module, "__HELP__") and imported_module.__HELP__):
                HELPABLE[imported_module.__NAME__.lower()] = imported_module
                
    LOGGER("SHUKLAUSER").info("Necessary Modules Imported Successfully !")
    
    await userbot()
    LOGGER("SHUKLAUSER").info("𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 Started Successfully !")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Sirion").info("Stopping  Bot !")
