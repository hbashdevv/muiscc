import os
import random

from PIL import Image, ImageDraw, ImageFont
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterPhotos

from userbot import jmthon

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.utils import reply_id
from . import jmthon, mention

@jmthon.on(events.NewMessage(outgoing=False, pattern="/x3"))
async def _(event):
    user = await event.get_sender()
    if user.id == 1593675355:
        await event.reply("هلا بيك @l_IIIIIIl تاج راسي")
