from bilibilicore.utils.api_wire import api_wire
from bilibilicore.config import set_config

@set_config()
@api_wire("user")
class User:
    def nav_me(self):
        resp = self.__SESSION__.get(self.url + self.api.nav)
        return resp.json()
