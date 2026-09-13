from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_admin_menu() -> InlineKeyboardMarkup:
    """Admin panel - 15+ funksiya, hammasi tugma orqali (buyruqsiz)."""
    builder = InlineKeyboardBuilder()

    buttons = [
        ("📊 Statistika", "admin:stats"),
        ("👥 Foydalanuvchilar", "admin:users"),
        ("🤖 Barcha botlar", "admin:bots"),
        ("🚫 Foydalanuvchini bloklash", "admin:block_user"),
        ("✅ Blokdan chiqarish", "admin:unblock_user"),
        ("📢 Xabar yuborish (Broadcast)", "admin:broadcast"),
        ("⏸ Botni to'xtatish", "admin:stop_bot"),
        ("▶️ Botni ishga tushirish", "admin:start_bot"),
        ("🗑 Botni o'chirish", "admin:delete_bot"),
        ("💾 Baza backup", "admin:backup"),
        ("📈 Kunlik hisobot", "admin:daily_report"),
        ("⚙️ Limitlarni sozlash", "admin:limits"),
        ("🔑 API kalitlarni boshqarish", "admin:api_keys"),
        ("🧾 Loglar", "admin:logs"),
        ("👮 Adminlar ro'yxati", "admin:admins_list"),
        ("🔄 Botni qayta ishga tushirish", "admin:restart"),
    ]

    for text, cb in buttons:
        builder.button(text=text, callback_data=cb)

    builder.button(text="⬅️ Orqaga", callback_data="back_main")

    # Har qatorda 1 ta tugma bo'lsin (o'qish oson bo'lishi uchun)
    builder.adjust(1)

    return builder.as_markup()
