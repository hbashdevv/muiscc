 # ======================================================================================================================================
# ping -> edited ping with pic by  @RR7PP
# كتابة الملف لسورس جمثون فقط ممنوع نسبه لنفسك
# تخمط دليل فشلك اخمط وكول اني مطور 😂😂

import os
from datetime import datetime

from userbot import jmthon

#
from . import hmention, reply_id

PING_PIC = os.environ.get("PING_PIC") or (
    "https://telegra.ph/file/5c8ae560c767c4d02c5cc.jpg"
)

JM_TXT = os.environ.get("PING_TEXT") or "تم اختيار بصمة 😂"

URL = os.environ.get("URL") or "https://t.me/fasngon/13114"


@jmthon.ar_cmd(pattern="ميمز$")
async def _(event):
    reply_to_id = await reply_id(event)
    start = datetime.now()
    cat = await edit_or_reply(
        event, "<b><i>  ❤️⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃟✨ انتــظر قـليـلاً... 🍀⃝⃝⃟🍂 </b></i>", "html"
    )
    end = datetime.now()
    await cat.delete()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{JM_TXT}<i><b>\n<code>{URL}<b>{hmention}</b>"
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
    else:
        await event.edit_or_reply(
            event, "<code>يجـب اضـافة متـغير `PING_PIC`  اولا  f<code>", "html"
        )


# ======================================================================================================================================
