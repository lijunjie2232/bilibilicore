import yaml

from bilibilicore.api import __MODULE_PATH__

# from .config_item import ConfigItem
from bilibilicore.utils import ConfigItem, singleton


@singleton
class Api(ConfigItem):
    __DATA__ = None

    def __init__(self):
        with open(
            __MODULE_PATH__ / "api.yaml",
            "r",
            encoding="utf-8",
        ) as f:
            self.__DATA__ = yaml.safe_load(f)
