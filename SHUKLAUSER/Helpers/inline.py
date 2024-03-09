from config import SUDO_USERS
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQuery


def inline_wrapper(func):
    async def wrapper(client, query: InlineQuery):
        if query.from_user.id not in SUDO_USERS:
            await client.answer_inline_query(
                query.id,
                cache_time=1,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="Sorry, You Can Not Use Me!",
                            input_message_content=InputTextMessageContent("You Can Not Access This"),
                        )
                    )
                ],
            )
        else:
            await func(client, query)
    return wrapper
