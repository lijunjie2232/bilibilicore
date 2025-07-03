def lazy_load(fun):
    """
    Use me to break circular dependencies.
    """

    prop_name = "_" + fun.__name__

    @property
    def lazy(self):
        try:
            return getattr(self, prop_name)
        except AttributeError:
            value = fun()
            setattr(self, prop_name, value)
            return value

    @lazy.setter
    def lazy(self, value):
        setattr(self, prop_name, value)

    return lazy
