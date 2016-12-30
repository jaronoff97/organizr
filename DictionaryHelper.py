
def value_exists(dictionary, key_search):
    for key in dictionary:
        if key == key_search:
            return True
    return False


def merge(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z


def getKeyFromValue(dictionary, search_value):
    for key, values in dictionary.items():
        for value in values:
            if value == search_value:
                return key
