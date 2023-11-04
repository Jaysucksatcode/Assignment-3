#SCT 211-0030/2022, Jayden Mathenge Muriithi
def Isleap(year):
    if (year%4==0):
        return True
    else:
        return False

year = int(input("Hello,Please enter the year you want to test: "))
Test=Isleap(year)
if(Test==True):
    print("The year is a leap year")
else:
    print("The year is not a leap year")