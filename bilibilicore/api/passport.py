from bilibilicore.utils import api_wire
from bilibilicore.config import set_config
from time import sleep
import os

@set_config()
@api_wire("passport")
class Passport:
    def get_qrcode(self):
        result = self.__SESSION__.get(
            self.url + self.api.qrcode.generate,
        ).json()

        return result

    def poll(self, params):
        try:
            resp = self.__SESSION__.get(
                self.url + self.api.qrcode.poll,
                params=params,
            )
            result = resp.json()
            assert result["code"] == 0
            data = result["data"]
            code = data["code"]
            if code == 0:
                # update cookie
                self.__SESSION__.cookies.update(
                    resp.cookies,
                )
                return 1
            elif code == 86038:
                print("二维码已失效")
                return -1
            elif code == 86090:
                print("二维码已扫码未确认")
                return 0
            elif code == 86101:
                print("未扫码")
            # else:
            #     raise Exception("未知错误")
            return False
        except Exception as e:
            print(e)
            return False

    def check_qrcode(self, qrcode_key):
        """
        0：扫码登录成功
        86038：二维码已失效
        86090：二维码已扫码未确认
        86101：未扫码
        """
        params = {
            "qrcode_key": qrcode_key,
        }
        while True:
            result = self.poll(params)
            if result:
                return
                pass
            sleep(3)
