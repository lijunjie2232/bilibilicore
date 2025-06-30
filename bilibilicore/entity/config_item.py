
class ConfigItem:
    __DATA__ = None

    def __init__(
        self,
        dict_config,
    ):
        self.__DATA__ = dict_config

    def __getattr__(
        self,
        name,
        if_not_found=None,
    ):
        if isinstance(name, str):
            name = tuple(name.split("."))
        data = self.__DATA__
        for i in name:
            if i in data:
                data = data[i]
            else:
                return if_not_found
        if isinstance(data, dict):
            return ConfigItem(data)
        elif isinstance(data, list):
            return [ConfigItem(i) for i in data]
        else:
            return data

    def __str__(self):
        return str(self.__DATA__)

    def __repr__(self):
        return self.__str__(self.__DATA__)
