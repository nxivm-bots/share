# https://t.me/Ultroid_Official/524

from pyrogram import __version__, Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.enums import ParseMode
from database.database import full_userbase
from bot import Bot
from config import OWNER_ID, ADMINS, CHANNEL, SUPPORT_GROUP, OWNER
from plugins.cmd import *

# Callback query handler
@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    data = query.data

    if data == "about":
        await query.message.edit_text(
            text=f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n"
                 f"○ Language : <code>Python3</code>\n"
                 f"○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n"
                 f"○ Source Code : <a href='https://youtu.be/BeNBEYc-q7Y'>Click here</a>\n"
                 f"○ Channel : @{CHANNEL}\n"
                 f"○ Support Group : @{SUPPORT_GROUP}</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔒 Close", callback_data="close")]]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except Exception as e:
            print(f"Error deleting reply-to message: {e}")

    elif data == "upi_info":
        await upi_info(client, query.message)

    elif data == "show_plans":
        await show_plans(client, query.message)
    """
    elif data == "refer":
        # Generate and send referral link
        user_id = query.from_user.id  # Get the user ID from the callback query
        bot_username = (await client.get_me()).username
        referral_link = f"https://t.me/{bot_username}?start=refer_{user_id}"
        verify_status = await db_verify_status(user_id)
        referral_count = verify_status.get("referral_count", 0)

        referral_message = (
            f"🔗 Your Personal Referral Link 🔗\n\n"
            f"📎 Link: {referral_link}\n\n"
            f"🤝 How it Works:\n"
            f"- Share this link with your friends.\n"
            f"- When they join, both of you get additional benefits!\n\n"
            f"📊 Your Referral Stats:\n"
            f"- Successful Referrals: {referral_count}\n\n"
            f"🎉 Keep sharing to enjoy more rewards!"
        )
        await query.message.reply_text(referral_message)

    elif data == "time":
        # Fetch and display user verification status
        user_id = query.from_user.id  # Get the user ID from the callback query
        verify_status = await db_verify_status(user_id)

        is_verified = verify_status.get("is_verified", False)
        verified_time = verify_status.get("verified_time", 0)
        referral_count = verify_status.get("referral_count", 0)
        referrer = verify_status.get("referrer", None)

        remaining_time = (
            max(0, int(verified_time - time.time())) if is_verified else "N/A"
        )
        remaining_hours = remaining_time // 3600 if isinstance(remaining_time, int) else "N/A"
        remaining_minutes = (remaining_time % 3600) // 60 if isinstance(remaining_time, int) else "N/A"

        referral_status = f"Yes (Referred by {referrer})" if referrer else "No Referrer"

        status_message = (
            f"🛠 Your Current Status 🛠\n\n"
            f"✅ Verified: {'Yes' if is_verified else 'No'}\n"
            f"⏰ Verification Time: {time.ctime(verified_time) if verified_time else 'Not Verified'}\n"
            f"🤝 Referral Status: {referral_status}\n"
            f"🕒 Remaining Usage Time: "
            f"{remaining_hours} hrs {remaining_minutes} mins" if is_verified else "N/A\n"
            f"📈 Successful Referrals: {referral_count}\n\n"
            f"💡 Tips: Share your referral link to extend your usage time!"
        )
        await query.message.reply_text(status_message)
    
    elif data == "time":
        # Since `status_command` expects `message`, you need to simulate this from the callback query
        user_id = query.from_user.id  # Get the user ID from the callback query
        verify_status = await db_verify_status(user_id)

        is_verified = verify_status.get("is_verified", False)
        verified_time = verify_status.get("verified_time", 0)
        referred_by = verify_status.get("referrer", None)

        status_message = (
            f"Your Status:\n"
            f"- Verified: {'Yes' if is_verified else 'No'}\n"
            f"- Verification Time: {time.ctime(verified_time) if verified_time else 'N/A'}\n"
            f"- Referred By: {referred_by if referred_by else 'None'}"
        )

        await query.message.reply(status_message)
        """

        
# https://t.me/Ultroid_Official/524


# ultroidofficial : YT



