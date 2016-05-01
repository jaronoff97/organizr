from Organize import Organize
from TypeOfOrg import TypeOfOrg
from clean_all import clean


def main():
    clean()
    organizr = Organize("Desktop", organization_method=TypeOfOrg.Filename)
    organizr.organize()

if __name__ == '__main__':
    main()
