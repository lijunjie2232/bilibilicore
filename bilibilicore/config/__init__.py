from .config import Config, set_config
from pathlib import Path

__MODULE_PATH__ = Path(__file__).parent.resolve()


# __CONFIG__ = Config()

__all__ = [
    "__MODULE_PATH__",
    "Config",
    "set_config",
]
