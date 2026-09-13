# Bot Yaratuvchi Bot (1-bosqich: poydevor)

## Fayllar tuzilmasi

```
bot-factory/
├── main.py              # Botni ishga tushiruvchi asosiy fayl
├── config.py             # .env / Railway Variables'dan sozlamalarni o'qiydi
├── database.py            # MongoDB bilan ishlash funksiyalari
├── requirements.txt       # Kerakli kutubxonalar
├── Procfile               # Railway'ga botni qanday ishga tushirishni aytadi
├── .env.example            # Qanday o'zgaruvchilar kerakligi namunasi
├── keyboards/
│   ├── main_menu.py        # Asosiy menyu tugmalari
│   └── admin_menu.py       # Admin panel tugmalari (15+ funksiya)
└── handlers/
    ├── start.py            # /start va asosiy menyu callback'lari
    └── admin.py            # Admin panel callback'lari
```

## Nima ishlaydi hozircha

- `/start` bosilganda foydalanuvchi MongoDB'ga yoziladi va asosiy menyu chiqadi.
- Asosiy menyuda 7 xil bot turi + "Mening botlarim" + "Yordam" tugmalari bor (hozircha placeholder javob beradi).
- Agar sizning Telegram ID'ingiz `ADMIN_IDS`da bo'lsa, "🛠 Admin panel" tugmasi chiqadi.
- Admin panelda 16 ta tugma bor: Statistika ishlaydi (bazadan foydalanuvchi/bot sonini o'qiydi), qolganlari hozircha "tez orada".

## Lokal komputerda sinab ko'rish (ixtiyoriy)

1. Python 3.11+ o'rnatilgan bo'lishi kerak.
2. Terminal ochib shu papkaga kiring va:
   ```
   pip install -r requirements.txt
   ```
3. `.env.example` faylni nusxalab, nomini `.env` ga o'zgartiring va ichiga haqiqiy token/URI'larni yozing.
4. Ishga tushiring:
   ```
   python main.py
   ```
5. Telegram'da botingizga `/start` yozing.

## GitHub'ga yuklash

1. GitHub'da yangi **repository** yarating (masalan `bot-factory`), Public yoki Private — farqi yo'q.
2. Terminalda shu papka ichida:
   ```
   git init
   git add .
   git commit -m "Birinchi versiya"
   git branch -M main
   git remote add origin https://github.com/USERNAME/bot-factory.git
   git push -u origin main
   ```
   (`.env` fayl `.gitignore` tufayli push bo'lmaydi — bu xavfsizlik uchun to'g'ri.)

## Railway'ga deploy qilish

1. https://railway.app → **New Project** → **Deploy from GitHub repo** → `bot-factory` repo'ni tanlang.
2. Railway avtomatik `requirements.txt` va `Procfile`ni topib, botni ishga tushirishga harakat qiladi — lekin avval Variables kerak.
3. Railway loyihasida **Variables** bo'limiga o'ting va qo'shing:
   - `BOT_TOKEN` = BotFather'dan olgan token
   - `MONGO_URI` = MongoDB Atlas connection string
   - `ADMIN_IDS` = sizning Telegram ID'ingiz (raqam)
   - `GEMINI_API_KEY` = Gemini API key
4. **Deploy** tugmasini bosing (yoki avtomatik boshlanadi). **Deployments** bo'limidan loglarni kuzatib, xatolik bo'lmasligini tekshiring.
5. Bot ishga tushgach, Telegram'da unga `/start` yuboring — asosiy menyu chiqishi kerak.

### Telegram ID'ni qanday bilib olish
Telegram'da **@userinfobot** ga `/start` yozing — u sizga ID raqamingizni chiqarib beradi. Shu raqamni `ADMIN_IDS`ga yozasiz.

## Keyingi bosqichlar (hali qilinmagan)

- Har bir "create:xxx" tugmasini bosganda haqiqiy bot yaratish jarayoni (token so'rash, MongoDB'ga yozish, yangi botni ishga tushirish).
- Kino / Stars / AI / Taxi / Valyuta / Tarjimon botlarining o'zlarining 30+ funksiyali kodi.
- Admin paneldagi qolgan 15 funksiyaning to'liq logikasi (broadcast, block, backup va h.k.).
- Gemini API'ni AI bot ichida ishlatish.
