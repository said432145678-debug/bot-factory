from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import ADMIN_IDS


def get_main_menu(user_id: int) -> InlineKeyboardMarkup:
    """Asosiy menyu - foydalanuvchi qaysi turdagi bot yaratmoqchi ekanini tanlaydi."""
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text="🎬 Kino bot", callback_data="create:movie"),
        InlineKeyboardButton(text="⭐️ Stars bot", callback_data="create:stars"),
    )
    builder.row(
        InlineKeyboardButton(text="🤖 AI bot", callback_data="create:ai"),
        InlineKeyboardButton(text="🚕 Taxi bot", callback_data="create:taxi"),
    )
    builder.row(
        InlineKeyboardButton(text="💱 Valyuta bot", callback_data="create:currency"),
        InlineKeyboardButton(text="🌐 Tarjimon bot", callback_data="create:translator"),
    )
    builder.row(
        InlineKeyboardButton(text="🧬 Bot Yaratuvchi (nusxa)", callback_data="create:factory"),
    )
    builder.row(
        InlineKeyboardButton(text="📁 Mening botlarim", callback_data="my_bots"),
        InlineKeyboardButton(text="ℹ️ Yordam", callback_data="help"),
    )

    if user_id in ADMIN_IDS:
        builder.row(
            InlineKeyboardButton(text="🛠 Admin panel", callback_data="admin_panel"),
        )

    return builder.as_markup()


def get_back_button(callback_data: str = "back_main") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ Orqaga", callback_data=callback_data)
    return builder.as_markup()
