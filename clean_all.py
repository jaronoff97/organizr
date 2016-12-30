import os.path
import os
import getpass
import shutil


def clean():
    basedir = '/Users/' + getpass.getuser() + '/Documents/Organized_Downloads/'
    counter = 0
    for filename in os.listdir(basedir):
        if not filename.startswith('.'):
            for file in os.listdir(basedir + filename):
                try:
                    shutil.move(
                        basedir + filename + '/' + file, '/Users/' +
                        getpass.getuser() + '/Desktop/' + file)
                except shutil.Error:
                    shutil.move(
                        basedir + filename + '/' + file, '/Users/' +
                        getpass.getuser() + '/Desktop/' + file + str(counter))
                counter += 1
        try:
            os.rmdir(basedir + filename)
        except OSError as ex:
            print("directory not empty")
            print(ex)
