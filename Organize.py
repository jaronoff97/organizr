import os.path
import datetime
import getpass
import os
import shutil
import TypeOfOrg


class Organize(object):
    """docstring for Organize"""
    endDir = '/Users/' + getpass.getuser() + '/Documents/Organized_Downloads/'

    def __init__(self, folder, organization_method=TypeOfOrg.Month):
        super(Organize, self).__init__()
        self.folder = folder
        self.organization_method = organization_method

    def organize(self):
        for filename in os.listdir(self.folder):
            if not filename.startswith('.'):
                modified = self.findModifiedTime(self.folder + filename)
                if not os.path.exists(Organize.endDir + modified):
                    os.makedirs(Organize.endDir + modified)
                shutil.move(
                    self.folder + filename, Organize.endDir +
                    modified + '/' + filename)

    def findModifiedTime(self, filename):
        theTime = os.path.getmtime(filename)
        return datetime.datetime.fromtimestamp(theTime).strftime(
            self.organization_method)
