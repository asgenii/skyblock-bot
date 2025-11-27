from aiogram import Bot, Dispatcher
import asyncio

from utils import ymlme
from telegram.router import router, permanent

async def main():
    bot = Bot(ymlme.main('telegram/config.yml')['token'])
    dp = Dispatcher()
    dp.include_router(router)
    asyncio.create_task(permanent(bot))
    print('[bot] online')
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        pass
