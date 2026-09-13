from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

# MongoDB'ga ulanish
client = AsyncIOMotorClient(MONGO_URI)
db = client["botfactory"]

# Kolleksiyalar (SQL'dagi "jadval"ga o'xshaydi)
users_col = db["users"]      # barcha foydalanuvchilar
bots_col = db["bots"]        # yaratilgan botlar ro'yxati
logs_col = db["logs"]        # amallar tarixi (admin panel uchun)


async def save_user(user_id: int, full_name: str, username: str | None):
    """Foydalanuvchi /start bosganda uni bazaga yozadi (bor bo'lsa yangilaydi)."""
    await users_col.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "full_name": full_name,
                "username": username,
            },
            "$setOnInsert": {"blocked": False},
        },
        upsert=True,
    )


async def get_users_count() -> int:
    return await users_col.count_documents({})


async def get_bots_count() -> int:
    return await bots_col.count_documents({})


async def is_user_blocked(user_id: int) -> bool:
    user = await users_col.find_one({"user_id": user_id})
    return bool(user and user.get("blocked"))
