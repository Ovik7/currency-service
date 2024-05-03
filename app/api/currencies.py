from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import CurrencyOut, CurrencyIn
from app.api import db_manager

currencies = APIRouter()

@currencies.post('/', response_model=CurrencyOut, status_code=201)
async def create_currency(payload: CurrencyIn):
    currency_id = await db_manager.add_currency(payload)

    response = {
        'id': currency_id,
        **payload.dict()
    }

    return response


@currencies.get('/', response_model=List[CurrencyOut])
async def get_currencies():
    return await db_manager.get_all_currency()


@currencies.get('/{id}/', response_model=CurrencyOut)
async def get_currency(id: int):
    company = await db_manager.get_currency(id)
    if not company:
        raise HTTPException(status_code=404, detail="currency not found")
    return company


@currencies.delete('/{id}/', response_model=None)
async def delete_currency(id: int):
    company = await db_manager.get_currency(id)
    if not company:
        raise HTTPException(status_code=404, detail="currency not found")
    return await db_manager.delete_currency(id)