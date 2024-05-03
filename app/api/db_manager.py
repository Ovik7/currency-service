from app.api.models import CurrencyIn, CurrencyOut
from app.api.db import currencies, database


async def add_currency(payload: CurrencyIn):
    query = currencies.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_currency():
    query = currencies.select()
    return await database.fetch_all(query=query)


async def get_currency(id):
    query = currencies.select().where(currencies.c.id == id)
    return await database.fetch_one(query=query)


async def delete_currency(id: int):
    query = currencies.delete().where(currencies.c.id == id)
    return await database.execute(query=query)

