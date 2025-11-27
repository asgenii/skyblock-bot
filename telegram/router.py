from aiogram import Router
from aiogram.types import Message
import asyncio

from skyblock.auction import background
from utils import jsonme

router = Router()

@router.message()
async def chat(message: Message):
    pass

async def permanent(bot):
    ah_notified = set()
    while True:
        for userid, user in jsonme.main('resources/users.json').items():
            result = background.main(user["API"], user["UUID"], ah_notified)
            if result.strip():
                await bot.send_message(chat_id = int(userid), text = result)
                
        await asyncio.sleep(10)