from aiogram import Router, F
from aiogram.types import CallbackQuery

from config import ADMIN_IDS
from database import get_users_count, get_bots_count
from keyboards.admin_menu import get_admin_menu
from keyboards.main_menu import get_back_button

router = Router()


def _is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS


@router.callback_query(F.data == "admin_panel")
async def open_admin_panel(callback: CallbackQuery):
    if not _is_admin(callback.from_user.id):
        await callback.answer("Sizda ruxsat yo'q ❌", show_alert=True)
        return

    await callback.message.edit_text(
        "🛠 <b>Admin panel</b>\n\nKerakli bo'limni tanlang:",
        reply_markup=get_admin_menu(),
    )
    await callback.answer()


@router.callback_query(F.data == "admin:stats")
async def admin_stats(callback: CallbackQuery):
    if not _is_admin(callback.from_user.id):
        await callback.answer("Ruxsat yo'q ❌", show_alert=True)
        return

    users_count = await get_users_count()
    bots_count = await get_bots_count()

    await callback.message.edit_text(
        f"📊 <b>Statistika</b>\n\n"
        f"👥 Foydalanuvchilar: {users_count}\n"
        f"🤖 Yaratilgan botlar: {bots_count}",
        reply_markup=get_back_button("admin_panel"),
    )
    await callback.answer()


# Qolgan 14 ta admin funksiya (broadcast, blok, backup va h.k.) uchun
# placeholder handler - hozircha "tez orada" deb javob beradi.
PLACEHOLDER_ADMIN_CALLBACKS = [
    "admin:users", "admin:bots", "admin:block_user", "admin:unblock_user",
    "admin:broadcast", "admin:stop_bot", "admin:start_bot", "admin:delete_bot",
    "admin:backup", "admin:daily_report", "admin:limits", "admin:api_keys",
    "admin:logs", "admin:admins_list", "admin:restart",
]


@router.callback_query(F.data.in_(PLACEHOLDER_ADMIN_CALLBACKS))
async def admin_placeholder(callback: CallbackQuery):
    if not _is_admin(callback.from_user.id):
        await callback.answer("Ruxsat yo'q ❌", show_alert=True)
        return

    await callback.message.edit_text(
        "Bu funksiya keyingi bosqichda qo'shiladi. ⏳",
        reply_markup=get_back_button("admin_panel"),
    )
    await callback.answer()
