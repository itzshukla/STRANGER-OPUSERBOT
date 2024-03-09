import aiohttp


async def post(url: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, *args, **kwargs) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
        return data


async def Pastebin(text):
    resp = await post("https://batbin.me/api/v2/paste", data=text)
    if not resp["success"]:
        return
    link = "https://batbin.me/" + resp["message"]
    return link