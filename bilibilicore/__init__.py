import sys

__VERSION__ = "0.0.1"

__PACKAGE_NAME__ = __package__.split(".")[0]
__PROJECT_ROOT__ = sys.modules[__PACKAGE_NAME__].__path__[0]

# from .utils import *
# from .api import *
# from .config import *

__all__ = [
    "__VERSION__",
    "__PACKAGE_NAME__",
    "__PROJECT_ROOT__",
]
