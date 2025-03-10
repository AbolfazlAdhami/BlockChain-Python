class Printable:
    '''A base class which implements printing functionallity'''

    def __repr__(self):
        return str(self.__dict__)
