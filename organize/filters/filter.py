class Filter:
    def run(self, path):
        """ Return an dict of parsed file properties (optional) """
        return NotImplementedError()

    def __str__(self):
        """ Return filter name and properties """
        return self.__class__.__name__

    def __repr__(self):
        return "<%s>" % str(self)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
