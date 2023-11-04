# SCT211-0030/2022, Jayden Mathenge Muriithi
def BillCalc(Totalbill, TipPercent, Headcount):
    Tip=Totalbill*(TipPercent / 100)
    TotalAmt=Totalbill + Tip
    AmountPerPerson = TotalAmt / Headcount
    return round(AmountPerPerson, 2)
#Headcount=no. of people
Totalbill = float(input("Hello, kindly Enter the total bill amount: "))
tip_option = input("Choose your tip percentage (10%, 12%, or 15%): ")
Headcount = int(input("Enter the number of people splitting the bill: "))

if tip_option == "10":
    TipPercent = 10
elif tip_option == "12":
    TipPercent = 12
elif tip_option == "15":
    TipPercent = 15
else:
    print("Invalid tip percentage. Please choose 10, 12, or 15.")
    exit()

AmountPerPerson = BillCalc(Totalbill, TipPercent, Headcount)
print("Each person should pay:",AmountPerPerson)