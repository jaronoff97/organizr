from Organize import Organize
from TypeOfOrg import TypeOfOrg


def main():
    organizr = Organize("Desktop", organization_method=TypeOfOrg.Filename)
    organizr.organize()

if __name__ == '__main__':
    main()
