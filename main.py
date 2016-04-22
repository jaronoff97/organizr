import os.path
import time
import datetime
import getpass
import glob
import os
import shutil


def main():
    directoryList = ['/Users/' + getpass.getuser() +
                     '/Downloads/', '/Users/' + getpass.getuser() + '/Desktop/']
    endDir = '/Users/' + getpass.getuser() + '/Documents/Organized_Downloads/'
    if not os.path.exists(endDir):
        os.makedirs(endDir)
    for directory in directoryList:
        for filename in os.listdir(directory):
            if not filename.startswith('.'):
                modified = findModifiedTime(directory + filename)
                if not os.path.exists(endDir + modified):
                    os.makedirs(endDir + modified)
                shutil.move(
                    directory + filename, endDir + modified + '/' + filename)


def findModifiedTime(filename):
    theTime = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(theTime).strftime('%Y-%m-%d')

if __name__ == '__main__':
    main()
