from aiogram import Router
from aiogram.types import Message
from datetime import datetime
import time, aiogram

from skyblock.auction import background
from utils import jsonme
from utils import ymlme

router = Router()

@router.message()
async def chat(message: Message):
    pass

async def permanent(bot):
    ah_notified = set()
    while True:
        for userid, user in jsonme.main('data/users.json').items():
            data = await background.main(user["API"], user["UUID"], ah_notified)
            if data != {}:
                log, message = '', ''
                for i in data.items():
                    log += f"[log | {datetime.now().strftime('%H:%M:%S')}] {user['nickname']}'s {i[1]['item']} was sold for {i[1]['price']}\n"
                    
                    # edit message down here
                    message += f"{i[1]['item']} was sold for {i[1]['price']}\n"

                try:
                    await bot.send_message(chat_id = int(userid), text = message)
                    print(log)
                except aiogram.exceptions.TelegramNetworkError as e:
                    print(f"Network error: {e}")