import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from config import BOT_TOKEN, WEBAPP_URL

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text="🎮 Открыть приложение", 
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]])
    await message.answer(
        "Привет! Я TaskTrackerRPG бот.\n"
        "Нажми кнопку, чтобы открыть игру:",
        reply_markup=keyboard
    )

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())