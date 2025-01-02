from aiohttp import web
from plugins import web_server
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, CHANNEL_ID, PORT
from database.database import *
import pyrogram.utils

pyrogram.utils.MIN_CHAT_ID = -999999999999
pyrogram.utils.MIN_CHANNEL_ID = -100999999999999

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # Fetch force-subscription channels from the database
        try:
            force_sub_channels = await get_all_force_sub_channels()
            self.force_sub_links = {}
            for channel in force_sub_channels:
                channel_id = channel["channel_id"]
                try:
                    chat = await self.get_chat(channel_id)
                    link = chat.invite_link
                    if not link:
                        link = await self.export_chat_invite_link(channel_id)
                    self.force_sub_links[channel_id] = link
                except Exception as e:
                    self.LOGGER(__name__).warning(f"Failed to fetch invite link for channel {channel_id}: {e}")
        except Exception as e:
            self.LOGGER(__name__).warning(f"Error fetching force-subscription channels from the database: {e}")
            sys.exit()

        # Check database channel access
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make sure bot is admin in DB Channel. Current CHANNEL_ID: {CHANNEL_ID}")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info("Bot is running... Created by https://t.me/ultroid_official")
        self.LOGGER(__name__).info(f"Bot username: @{usr_bot_me.username}")
        self.LOGGER(__name__).info(f""" \n\n 
        bot running...!
(っ◔◡◔)っ ♥ ULTROIDOFFICIAL ♥
░╚════╝░░╚════╝░╚═════╝░╚══════╝
                                         """)
        self.username = usr_bot_me.username

        # Web server setup
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. https://t.me/ultroid_official.")
