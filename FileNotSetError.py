
class FileNotSetError(Exception):
    """docstring for FileNotSetError"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
