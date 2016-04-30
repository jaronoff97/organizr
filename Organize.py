import os.path
import datetime
import getpass
import os
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
        for key, values in accepted_files.items():
            for value in values:
                if value in filename.ascii_lowercase:
                    if not os.path.exists(Organize.endDir + key):
                        os.makedirs(Organize.endDir + key)
                    shutil.move(
                        self.folder + filename, Organize.endDir +
                        key + '/' + filename)
