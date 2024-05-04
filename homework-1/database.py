import aiosqlite

async def create_table():
    async with aiosqlite.connect("users.db") as db:
        await db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, username TEXT)")
        await db.commit()

async def add_user(user_id, username):
    async with aiosqlite.connect("users.db") as db:
        await db.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
        await db.commit()
