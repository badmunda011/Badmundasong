from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from youtubesearchpython import VideosSearch
from Royalkifeelings.callmusic.config import GROUP_SUPPORT as Royalboyamit


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0


def audio_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="➷ 𝐔𝗽𝗱𝗮𝘁𝗲𝐒 ➹", url=f"https://t.me/BAD_MUNDA_0"),
      InlineKeyboardButton(text="➹ 𝐒𝘂𝗽𝗽𝗼𝗿𝐓 ➷", url=f"https://t.me/THE_DRAMA_CLUB_01"),
    ],
    [
      InlineKeyboardButton(text="✯ 𝗢𝘄𝗻𝗲𝗿'𝘅𝗗 ✯", url=f"https://t.me/ll_JATT_USTAAD_ll"),
    ],
    [
      InlineKeyboardButton(text="★ 𝐂ʟᴏ𝐬ᴇ ★", callback_data=f'cls'),
    ],
  ]
  return buttons

def stream_markup(user_id, dlurl):
  buttons = [
    [
      InlineKeyboardButton(text="➷ 𝐔𝗽𝗱𝗮𝘁𝗲𝐒 ➹", url=f"https://t.me/BAD_MUNDA_0"),
      InlineKeyboardButton(text="➹ 𝐒𝘂𝗽𝗽𝗼𝗿𝐓 ➷", url=f"https://t.me/THE_DRAMA_CLUB_01"),
    ],
    [
      InlineKeyboardButton(text="✯ 𝗢𝘄𝗻𝗲𝗿'𝘅𝗗 ✯", url=f"https://t.me/ll_JATT_USTAAD_ll"),
    ], 
    [
      InlineKeyboardButton(text="★ 𝐂ʟᴏ𝐬ᴇ ★", callback_data=f'cls'),
    ],
  ]
  return buttons

def menu_markup(user_id):
  buttons = [
     [InlineKeyboardButton(text="🔇", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="ᴜᴩᴅᴀᴛᴇs", url=f"https://t.me/spotif_ymusic31_bot"),
      InlineKeyboardButton(text="🔊", callback_data=f'cbunmute | {user_id}')],
  ]
  return buttons

def song_download_markup(videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text="⬇️ ᴀᴜᴅɪᴏ",
                callback_data=f"gets audio|{videoid}",
            ),
            InlineKeyboardButton(
                text="⬇️ ᴠɪᴅᴇᴏ",
                callback_data=f"gets video|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="★ 𝐁ᴀᴄᴋ ★",
                callback_data="cbhome",
            )
        ],
    ]
    return buttons

close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "★ 𝐂ʟᴏsᴇ ★", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "★ 𝐁ᴀᴄᴋ ★", callback_data="cbmenu"
      )
    ]
  ]
)
