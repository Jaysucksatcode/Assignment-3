from datetime import datetime

def AgeCalc(Year, month, day):
    current_date = datetime.now()
    birth_date = datetime(Year, month, day)
    age = current_date - birth_date
    years = age.days // 365
    remaining_days = age.days % 365
    months = remaining_days // 30
    days = remaining_days % 30
    return years, months, days
Greeting = input("Hello, kindly enter your name: ")
Year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))
if(month>12 or month<1 or day<0 or day>31):
    print("Invalid Parameters, please enter valid data(Months shouldn't exceed 12 or be 0 and days shouldn't exceed 31 or be 0 )")
else:
    Age=AgeCalc(Year,month,day)
    print("Dear "+Greeting+" Your age is: ",Age)