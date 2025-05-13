from aiogram import Router, types
from aiogram.filters import Command
from bot.db import init_db
import aiosqlite

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    # Инициализируем БД (на всякий случай)
    await init_db()

    keyboard = types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        types.InlineKeyboardButton("➕ Создать задачу", callback_data="create_task"),
        types.InlineKeyboardButton("✅ Отметить выполнение", callback_data="mark_done"),
        types.InlineKeyboardButton("📊 Посмотреть прогресс", callback_data="view_stats"),
    ]
    keyboard.add(*buttons)
    await message.answer("Выберите действие:", reply_markup=keyboard)

@router.callback_query(lambda c: c.data == "create_task")
async def cb_create_task(c: types.CallbackQuery):
    # Здесь будет углублённая логика через FSM (скажу чуть позже)
    await c.answer("Начинаем создание задачи…")

@router.callback_query(lambda c: c.data == "mark_done")
async def cb_mark_done(c: types.CallbackQuery):
    await c.answer("Список задач для отметки…")

@router.callback_query(lambda c: c.data == "view_stats")
async def cb_view_stats(c: types.CallbackQuery):
    await c.answer("Загружаю вашу статистику…")
