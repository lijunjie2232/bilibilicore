import threading

_LOCK = threading.Lock()


def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if not hasattr(cls, "_instance_lock"):
            with _LOCK:
                if not hasattr(cls, "_instance_lock"):
                    setattr(
                        cls,
                        "_instance_lock",
                        threading.Lock(),
                    )
        if cls not in _instance:
            with cls._instance_lock:
                if cls not in _instance:
                    _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton
