class simpleCalc:
    def Add(self,num1,num2):
        return num1+num2
    
    def Diff(self,num1,num2):
        return num1-num2
    
    def multiply(self,num1,num2):
        return num1*num2
    
    def Div(slef,num1,num2):
        if num2 == 0:
            return "cannot divide by 0"
        else:
           return num1/num2
calculator=simpleCalc()

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

operation = input("Choose your desired opearation(+,-,*,/): ")

if operation == '+':
    result=calculator.Add(num1,num2)
elif operation =='-':
    result=calculator.Diff(num1,num2)
elif operation=='*':
    result=calculator.multiply(num1,num2)
elif operation=='/':
    result=calculator.Div(num1,num2)
else:
    result="Invalid input"

print("Your output is:",result)