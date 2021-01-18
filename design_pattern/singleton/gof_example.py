class Logger:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
        return cls._instance


#log = Logger() # throws error
log1 = Logger.instance()
log2 = Logger.instance()
print('Are they the same object?', log1 is log2)