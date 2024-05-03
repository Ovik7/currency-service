import pytest
from app.api.models import CurrencyIn, CurrencyOut

currencies = CurrencyIn(
    name='Bitcoin',
    code='BTC',
    max_count='21000000',
    area='Blockchain'
)


def test_create_currency(currencies: CurrencyIn = currencies):
    assert dict(currencies) == {'name': currencies.name,
                                'code': currencies.code,
                                'max_count': currencies.max_count,
                                'area': currencies.area
                                }


def test_update_currency_age(currencies: CurrencyIn = currencies):
    currency_upd = CurrencyOut(
        name='Bitcoin',
        code='BTC',
        max_count='21000000',
        area='Blockchain',
        id=1
    )
    assert dict(currency_upd) == {'name': currencies.name,
                                  'code': currencies.code,
                                  'max_count': currencies.max_count,
                                  'area': currencies.area,
                                  'id': currency_upd.id
                                  }


def test_update_currency_genre(currencies: CurrencyIn = currencies):
    currency_upd = CurrencyOut(
        name='Bitcoin',
        code='BTC',
        max_count='21000000',
        area='Blockchain',
        id=1
    )
    assert dict(currency_upd) == {'name': currencies.name,
                                  'code': currencies.code,
                                  'max_count': currencies.max_count,
                                  'area': currencies.area,
                                  'id': currency_upd.id
                                  }
