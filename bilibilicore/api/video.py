import os

from bilibilicore.config import set_config
from bilibilicore.utils.api_wire import api_wire


@set_config()
@api_wire("video")
class Video:

    def get_playurl(
        self,
        id,
        cid,
        fnval=16,
    ):
        id = str(id)
        params = {
            "fnval": fnval,
            "avid" if id.isdigit() else "bvid": id,
            "cid": cid,
        }
        result = self.__SESSION__.get(
            self.url + self.api.playurl,
            params=params,
        )
        assert result.status_code == 200
        assert result.json()["code"] == 0
        return result.json()
