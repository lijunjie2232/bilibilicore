# api/session.py

import requests

_shared_session = None
UA = "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0 BiliDroid/9.3.2 (bbcallen@gmail.com)"
REFERER = "https://www.bilibili.com"


def get_session(
    ua=UA,
    referer=REFERER,
):
    global _shared_session
    if _shared_session is None:
        _shared_session = requests.Session()
        # Optional: Set default headers, auth, hooks, etc.
        _shared_session.headers.update(
            {
                "User-Agent": ua,
                "referer": referer,
            }
        )
    return _shared_session


def set_session(session):
    global _shared_session
    _shared_session = session


def close_session():
    global _shared_session
    if _shared_session:
        _shared_session.close()
    _shared_session = None
