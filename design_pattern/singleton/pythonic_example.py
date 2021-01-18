class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('creating the object')
            cls._instance =  super(Logger,cls).__new__(cls)
        return cls._instance

log1 = Logger()
log2 = Logger()
print('Are they the same object?', log1 is log2)
