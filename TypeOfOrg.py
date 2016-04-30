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
