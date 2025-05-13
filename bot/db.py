import aiosqlite
import os

DB_PATH = os.getenv("DB_PATH", "tracker.db")

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        # Пользователи
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                telegram_id INTEGER UNIQUE,
                username TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)
        # Задачи
        await db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                user_id INTEGER REFERENCES users(id),
                title TEXT,
                category TEXT,
                due_date TEXT,
                xp INTEGER DEFAULT 0,
                status TEXT DEFAULT 'active',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)
        # Лог
        await db.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY,
                user_id INTEGER REFERENCES users(id),
                action TEXT,
                metadata TEXT,
                ts TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)
        await db.commit()
