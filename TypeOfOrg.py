from enum import Enum


class TypeOfOrg(Enum):
    Day = 0
    Month = 1
    Year = 2

    def modifiedTimeString(self):
        if self.value is TypeOfOrg.Day:
            return '%Y-%m-%d'
        if self.value is TypeOfOrg.Month:
            return '%Y-%m'
        if self.value is TypeOfOrg.Year:
            return '%Y'
