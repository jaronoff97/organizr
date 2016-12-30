from Organize import Organize
from TypeOfOrg import TypeOfOrg
from clean_all import clean


def main():
    clean()
    downloads_organizr = Organize(
        "Downloads", organization_method=TypeOfOrg.Filename)
    downloads_organizr.organize()
    desktop_organizr = Organize(
        "Desktop", organization_method=TypeOfOrg.Filename)
    desktop_organizr.organize()

if __name__ == '__main__':
    main()
