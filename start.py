from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from database import save_user
from keyboards.main_menu import get_main_menu, get_back_button

router = Router()

WELCOME_TEXT = (
    "👋 Assalomu alaykum, {name}!\n\n"
    "Men <b>Bot Yaratuvchi Bot</b>man.\n"
    "Quyidagi menyudan qaysi turdagi bot yaratmoqchi ekaningizni tanlang.\n\n"
    "Hammasi tugmalar orqali ishlaydi — buyruq yozish shart emas 👇"
)

# Telegram qoidasiga ko'ra, foydalanuvchi bot bilan suhbatni
# har doim /start bilan boshlaydi (bu Telegram platformasining o'zi talab qiladigan
# yagona buyruq). Undan keyingi HAMMA narsa faqat tugmalar orqali bo'ladi.


@router.message(CommandStart())
async def cmd_start(message: Message):
    await save_user(
        user_id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username,
    )
    await message.answer(
        WELCOME_TEXT.format(name=message.from_user.full_name),
        reply_markup=get_main_menu(message.from_user.id),
    )


@router.callback_query(F.data == "back_main")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(
        WELCOME_TEXT.format(name=callback.from_user.full_name),
        reply_markup=get_main_menu(callback.from_user.id),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("create:"))
async def create_bot_placeholder(callback: CallbackQuery):
    bot_type = callback.data.split(":")[1]

    names = {
        "movie": "🎬 Kino bot",
        "stars": "⭐️ Stars bot",
        "ai": "🤖 AI bot",
        "taxi": "🚕 Taxi bot",
        "currency": "💱 Valyuta bot",
        "translator": "🌐 Tarjimon bot",
        "factory": "🧬 Bot Yaratuvchi bot (nusxa)",
    }

    await callback.message.edit_text(
        f"{names.get(bot_type, 'Bot')} yaratish moduli hozircha tayyorlanmoqda.\n\n"
        "Keyingi bosqichda bu yerga token so'rash va bazaga yozish logikasi qo'shiladi.",
        reply_markup=get_back_button(),
    )
    await callback.answer()


@router.callback_query(F.data == "my_bots")
async def my_bots_placeholder(callback: CallbackQuery):
    await callback.message.edit_text(
        "📁 Sizning botlaringiz ro'yxati bu yerda ko'rinadi.\n"
        "(Hozircha bo'sh — bot yaratish moduli qo'shilgach ishlaydi)",
        reply_markup=get_back_button(),
    )
    await callback.answer()


@router.callback_query(F.data == "help")
async def help_placeholder(callback: CallbackQuery):
    await callback.message.edit_text(
        "ℹ️ Yordam\n\n"
        "Bu bot orqali siz o'zingizga kerakli Telegram botni bir necha tugma bosish "
        "bilan yaratasiz. Har bir bot turi uchun alohida sozlamalar bo'ladi.",
        reply_markup=get_back_button(),
    )
    await callback.answer()
