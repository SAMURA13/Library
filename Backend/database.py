import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import URL, create_engine,text
from config import settings

# Синхронное подключение к БД
sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    # echo=True,
    )

# Асинхронное подключение к БД
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    # echo=True,
    )

# Синхронный запрос к БД
with sync_engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f'{res.first()=}')

# Асинхроннный запрос к БД
async def get_123():    
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f'{res.first()=}')
        
asyncio.run(get_123())