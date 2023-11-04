#SCT 211-0030/2022, Jayden Mathenge Muriithi
def calculate_bmi(weight, height):
    return weight / (pow(height,2))

def BMIcheck(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal Weight"
    else:
        return "Overweight"

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

result = BMIcheck(bmi)
print("Your BMI is:",bmi)
print("You are:",result)