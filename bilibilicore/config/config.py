from bilibilicore.utils import (
    get_session,
    set_session,
    check_and_mkdir,
    get_app_data_dir,
    singleton,
    ConfigItem,
)

# from bilibilicore.entity import ConfigItem
from functools import wraps
from pathlib import Path
from shutil import copy
import pickle
import atexit  # 新增：导入 atexit 模块
import toml
import os

__CONFIG_TEMPLATE_PATH__ = Path(__file__).parent.resolve() / "config.toml.example"


@singleton
class Config:
    __CONFIG__ = None
    __SESSION__ = None

    @property
    def session(self):
        return self.__SESSION__

    @property
    def config(self):
        return self.__CONFIG__

    def __init__(self):
        self._app_data_dir = get_app_data_dir(
            "bilibili-core",
        )
        self._cache_dir = self._app_data_dir / "cache"
        self._config_dir = self._app_data_dir / "config"
        self._config_file = self._config_dir / "config.toml"
        self._session_path = self._app_data_dir / "ses.bin"
        self._init_config_dir()
        self._init_config()
        self._session_init()

        # 新增：注册 atexit 回调函数，确保在程序退出时保存会话
        atexit.register(self._save_session_on_exit)
        atexit.register(self._save_config_on_exit)

    @property
    def cache_dir(self):
        return self._cache_dir

    @property
    def config_dir(self):
        return self._config_dir

    def _session_init(self):
        # 检查 session 文件是否存在
        try:
            with open(
                self._session_path,
                "rb",
            ) as f:
                self.__SESSION__ = pickle.load(f)
            set_session(self.__SESSION__)
        except Exception as e:
            print(f"Failed to load session from {self._session_path}: {e}")
            self.__SESSION__ = get_session()  # 修改：将会话赋值给实例变量

    def _save_session_on_exit(self):
        """在程序退出时保存会话到文件"""
        try:
            with open(
                self._session_path,
                "wb",
            ) as f:
                pickle.dump(self.__SESSION__, f)
            print(f"Session saved to {self._session_path}")
        except Exception as e:
            print(f"Failed to save session to {self._session_path}: {e}")

    def _init_config_dir(self):
        for d in [
            self._app_data_dir,
            self._cache_dir,
            self._config_dir,
        ]:
            assert check_and_mkdir(d), f"Failed to check or create directory: {d}"

    def _init_config(self):
        if not self._config_file.is_file():
            copy(
                __CONFIG_TEMPLATE_PATH__,
                self._config_file,
            )
        try:
            self.__CONFIG__ = toml.load(self._config_file)
        except Exception as e:
            print(f"Failed to load config from {self._config_file}: {e}")

    def _save_config_on_exit(self):
        try:
            with open(
                self._config_file,
                "w",
            ) as f:
                toml.dump(
                    self.__CONFIG__,
                    f,
                )
            print(f"Config saved to {self._config_file}")
        except Exception as e:
            print(f"Failed to save config to {self._config_file}: {e}")

    def __getattr__(self, name):
        """
        当访问不存在的属性时，尝试从 self.__CONFIG__ 中查找对应的键值对。
        如果找到，则返回对应值；否则返回 None 或抛出 AttributeError。
        """
        # if isinstance(name, str):
        #     name = tuple(name.split("."))
        # data = self.__CONFIG__
        # for i in name:
        #     if i in data:
        #         data = data[i]
        #     else:
        #         return None  # 返回 None 表示未找到
        return getattr(ConfigItem(self.__CONFIG__), name)


_config_instance = Config()


def set_config(wire_keys=["__CONFIG__", "__SESSION__"]):
    def decorator(cls):
        def configWrapper(*args, **kwargs):
            obj = cls(*args, **kwargs)
            for key in wire_keys:
                value = getattr(_config_instance, key)
                setattr(obj, key, value)
            return obj

        return configWrapper

    return decorator
