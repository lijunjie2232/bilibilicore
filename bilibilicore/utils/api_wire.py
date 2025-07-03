def api_wire(section_name):
    def decorator(cls):
        from bilibilicore.entity import Api

        api_section = getattr(Api(), section_name)

        original_init = cls.__init__

        def __wrapper_init__(self, *args, **kwargs):
            self.url = api_section.url
            self.api = api_section.api
            original_init(self, *args, **kwargs)

        cls.__init__ = __wrapper_init__
        return cls

    return decorator
