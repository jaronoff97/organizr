class TypeOfOrg:
    Day = 0
    Month = 1
    Year = 2
    Filename = 3

    def modifiedTimeString(self):
        if self is TypeOfOrg.Day:
            return '%Y-%m-%d'
        if self is TypeOfOrg.Month:
            return '%Y-%m'
        if self is TypeOfOrg.Year:
            return '%Y'

    def orgFromInt(i):
        if i == 0:
            return TypeOfOrg.Day
        if i == 1:
            return TypeOfOrg.Month
        if i == 2:
            return TypeOfOrg.Year
        if i == 3:
            return TypeOfOrg.Filename
