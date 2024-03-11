class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_dash(cls,string):
          return cls(*string.split("-"))

    @classmethod
    def sec_from_dash(cls,string):
        name=string.split('-')
        return cls(name[0],name[1],name[2])

date1=Date.from_dash("2008-12-5")
print(date1.year)
Date2=Date.sec_from_dash('2003-5-11')
print(Date2.day)
#Output: 2008