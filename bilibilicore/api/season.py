import os
from time import sleep

from bilibilicore.config import set_config
from bilibilicore.utils.api_wire import api_wire


@set_config()
@api_wire("season")
class Season:

    def seasons_archives_list(
        self,
        season_id,
        reverse=False,
        page_size=30,
        page_num=1,
    ):
        result = self.__SESSION__.get(
            self.url + self.api.seasons_archives_list,
            params={
                "season_id": str(season_id),
                "reverse": reverse,
                "page_size": page_size,
                "page_num": page_num,
            },
        )
        assert result.status_code == 200
        assert result.json()["code"] == 0, result.json()["message"]
        return result.json()

    def get_view(
        self,
        id,
    ):
        id = str(id)
        params = {
            "aid" if id.isdigit() else "bvid": id,
        }
        result = self.__SESSION__.get(
            self.url + self.api.view,
            params=params,
        )
        assert result.status_code == 200
        assert result.json()["code"] == 0
        return result.json()

    def get_detail(
        self,
        id,
    ):
        id = str(id)
        params = {
            "aid" if id.isdigit() else "bvid": id,
        }
        result = self.__SESSION__.get(
            self.url + self.api.detail,
            params=params,
        )
        assert result.status_code == 200
        assert result.json()["code"] == 0
        return result.json()
