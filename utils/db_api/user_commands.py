from main.database_set import database
from main.models import users


async def get_user(chat_id: int):
    try:
        query = users.select().where(
           users.c.chat_id == chat_id
        )
        user = await database.fetch_one(query=query)
        return user
    except Exception as exc:
        print(exc)
        return None