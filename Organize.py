import os.path
import datetime
import getpass
import os
import shutil
from TypeOfOrg import TypeOfOrg
from Accepted_Files import accepted_files
import DictionaryHelper as dictionary
from FileNotSetError import FileNotSetError


class Organize(object):
    """docstring for Organize"""
    baseDir = '/Users/' + getpass.getuser() + '/'
    endDir = '/Users/' + getpass.getuser() + '/Documents/Organized_Downloads/'

    def __init__(self, folder,
                 organization_method=TypeOfOrg.Month,
                 show_all_keys=True):
        super(Organize, self).__init__()
        if not os.path.exists(Organize.endDir):
            os.makedirs(Organize.endDir)
        self.folder = Organize.baseDir + folder + '/'
        self.organization_method = organization_method
        self.all_keys = {}
        self.show_all_keys = show_all_keys

    def organize(self):
        if self.folder is None:
            raise FileNotSetError("FOLDER NOT SET!")
        for filename in os.listdir(self.folder):
            if not filename.startswith('.'):
                if self.organization_method is not TypeOfOrg.Filename:
                    self.moveFileByTime(filename)
                elif self.organization_method is TypeOfOrg.Filename:
                    self.moveFileByName(filename)
        if self.show_all_keys:
            print(self.all_keys)

    def findModifiedTime(self, filename):
        theTime = os.path.getmtime(filename)
        return datetime.datetime.fromtimestamp(theTime).strftime(
            TypeOfOrg.modifiedTimeString(self.organization_method))

    def moveFileByTime(self, filename):
        final_path = self.folder + filename
        modified = self.findModifiedTime(final_path)
        if not os.path.exists(Organize.endDir + modified):
            os.makedirs(Organize.endDir + modified)
        self.moveAndRemove(
            final_path, Organize.endDir +
            modified + '/' + filename)

    def moveFileByName(self, filename):
        moved = False
        final_path = self.folder + filename
        for key, values in accepted_files.items():
            if not os.path.exists(Organize.endDir + key):
                os.makedirs(Organize.endDir + key)
            if not os.path.exists(Organize.endDir + 'Other'):
                os.makedirs(Organize.endDir + 'Other')
            for value in values:
                try:
                    if value in filename.lower() and os.path.isfile(
                            final_path):
                        self.moveAndRemove(
                            final_path, Organize.endDir +
                            key + '/' + filename)
                        moved = True
                except Exception as e:
                    print("ERROR {0}".format(e))
        if not moved:
            contents = self.countContents(final_path)
            common_key = []
            if not contents:
                pass
            else:
                max_val = max(contents.items(), key=lambda x: int(x[1]))[0]
                common_key = dictionary.getKeyFromValue(
                    accepted_files, max_val)
            if common_key:
                self.moveAndRemove(final_path, Organize.endDir +
                                   common_key + '/' + filename)
            else:
                self.moveAndRemove(final_path, Organize.endDir +
                                   'Other' + '/' + filename)

    def moveAndRemove(self, filename, destination):
        removed = False
        if os.path.isdir(filename):
            if len([name for name in os.listdir(filename) if (os.path.isfile(
                    os.path.join(filename, name)) or
                    os.path.isdir(os.path.join(filename, name))) and
                    not name.startswith('.')]) == 0:
                shutil.rmtree(filename)
                print("REMOVED {0}".format(filename))
                removed = True
        if not removed:
            shutil.move(filename, destination)

    def countContents(self, folder):
        file_types = {}
        if os.path.isdir(folder):
            for file in os.listdir(folder):
                key = os.path.splitext(file)[1]
                if key is '':
                    continue
                if (os.path.isdir(folder + '/' + file) and
                        not os.path.isfile(folder + '/' + file)):
                    internal_files = self.countContents(folder + '/' + file)
                    file_types = dictionary.merge(
                        file_types.copy(),
                        internal_files)
                else:
                    if dictionary.value_exists(file_types, key):
                        file_types[key] = file_types.get(key, 0) + 1
                    else:
                        file_types[key] = 1
                    if self.show_all_keys:
                        if dictionary.value_exists(self.all_keys, key):
                            self.all_keys[key] = self.all_keys.get(key, 0) + 1
                        else:
                            self.all_keys[key] = 1
        return file_types
