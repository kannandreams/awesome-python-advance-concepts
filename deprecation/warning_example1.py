import warnings

#refer this link to learn about warnings categories
#https://docs.python.org/3/library/warnings.html


warnings.simplefilter('default') # also can be enabled through command line flag  python3 -Wd

class WarningExample:
    def __init__(self,input:list):
        self.input = input

    def sortv1(self):
        warnings.warn(
            "sortv1 is deprecated, use sortv3 instead",
            DeprecationWarning
        )
        return sorted(self.input)

    def sortv2(self):
        warnings.warn(
            "sortv2 will be deprecated in version 3, use sortv3 instead",
             PendingDeprecationWarning
        )
        return sorted(self.input)

    def sortv3(self):
        return sorted(self.input)


if __name__ == '__main__':
    example = WarningExample([10,4,2,1,5])

    print(example.sortv1())
    print(example.sortv2())
    print(example.sortv3())
