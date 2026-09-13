import os
from dotenv import load_dotenv

# Lokal kompyuterda ishlaganda .env fayldan o'qiydi.
# Railway'da esa bu qatorlar hech narsa qilmaydi - Railway o'zi
# Environment Variables bo'limidagi qiymatlarni beradi.
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ADMIN_IDS masalan: "123456789,987654321" ko'rinishida Railway'ga yoziladi
_admin_ids_raw = os.getenv("ADMIN_IDS", "")
ADMIN_IDS = [int(x.strip()) for x in _admin_ids_raw.split(",") if x.strip()]

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN topilmadi! .env faylga yoki Railway Variables'ga qo'shing.")
if not MONGO_URI:
    raise ValueError("MONGO_URI topilmadi! .env faylga yoki Railway Variables'ga qo'shing.")
