import os.path
import datetime
import getpass
import os
import operator
import shutil
from TypeOfOrg import TypeOfOrg
from Accepted_Files import accepted_files


class Organize(object):
    """docstring for Organize"""
    baseDir = endDir = '/Users/' + getpass.getuser() + '/'
    endDir = '/Users/' + getpass.getuser() + '/Documents/Organized_Downloads/'

    def __init__(self, folder, organization_method=TypeOfOrg.Month):
        super(Organize, self).__init__()
        if not os.path.exists(Organize.endDir):
            os.makedirs(Organize.endDir)
        self.folder = Organize.baseDir + folder + '/'
        self.organization_method = organization_method

    def organize(self):
        for filename in os.listdir(self.folder):
            if not filename.startswith('.'):
                if self.organization_method is not TypeOfOrg.Filename:
                    self.moveFileByTime(filename)
                elif self.organization_method is TypeOfOrg.Filename:
                    self.moveFileByName(filename)

    def findModifiedTime(self, filename):
        theTime = os.path.getmtime(filename)
        return datetime.datetime.fromtimestamp(theTime).strftime(
            TypeOfOrg.modifiedTimeString(self.organization_method))

    def moveFileByTime(self, filename):
        modified = self.findModifiedTime(self.folder + filename)
        if not os.path.exists(Organize.endDir + modified):
            os.makedirs(Organize.endDir + modified)
        shutil.move(
            self.folder + filename, Organize.endDir +
            modified + '/' + filename)

    def moveFileByName(self, filename):
        moved = False
        for key, values in accepted_files.items():
            if not os.path.exists(Organize.endDir + key):
                os.makedirs(Organize.endDir + key)
            if not os.path.exists(Organize.endDir + 'Other'):
                os.makedirs(Organize.endDir + 'Other')
            for value in values:
                try:
                    if value in filename.lower():
                        shutil.move(
                            self.folder + filename, Organize.endDir +
                            key + '/' + filename)
                        moved = True
                except Exception as e:
                    # print(e)
                    pass
        if not moved:
            contents = self.countContents(self.folder + filename)
            # print(contents)
            common_key = []
            if not contents:
                pass
            else:
                max_val = max(contents.items(), key=operator.itemgetter(1))[0]
                common_key = self.getKeyFromValue(accepted_files, max_val)
            if common_key:
                shutil.move(self.folder + filename, Organize.endDir +
                            common_key + '/' + filename)
            else:
                shutil.move(self.folder + filename, Organize.endDir +
                            'Other' + '/' + filename)

    def value_exists(self, dictionary, key_search):
        for key in dictionary:
            if key == key_search:
                return True
        return False

    def merge(self, x, y):
        '''Given two dicts, merge them into a new dict as a shallow copy.'''
        z = x.copy()
        z.update(y)
        return z

    def getKeyFromValue(self, dictionary, search_value):
        for key, values in dictionary.items():
            for value in values:
                if value == search_value:
                    return key

    def countContents(self, folder):
        file_types = {}
        if os.path.isdir(folder):
            for file in os.listdir(folder):
                key = os.path.splitext(file)[1]
                if os.path.isdir(folder + '/' + file):
                    file_types = self.merge(
                        file_types, self.countContents(folder + '/' + file))
                else:
                    if self.value_exists(file_types, key):
                        file_types[key] = file_types.get(key, 0) + 1
                    else:
                        file_types[key] = 1
        return file_types
