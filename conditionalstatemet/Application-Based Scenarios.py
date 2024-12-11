# Electricity bill  
units = 150
if units <= 100:
    bill = units * 5
    print("Electricity bill: ", bill)
elif units > 100 and units <= 200:
    bill = units * 10
    print("Electricity bill: ", bill)
else:
    bill = units * 15
    print("Electricity bill: ", bill)


#Season finder  
month = "June"
if month in ("December", "January", "February"):
    print("Season: Winter")
elif month in ("March", "April", "May"):
    print("Season: Spring")
elif month in ("June", "July", "August"):
    print("Season: Summer")
elif month in ("September", "October", "November"):
    print("Season: Autumn")
else:
    print("Invalid month")


#Password validation
password = "password@123"
if len(password) >= 8 and "@" in password:
    print("Password is valid")
else:
    print("Password is not valid. It should be at least 8 characters and contain '@'.")




#BMI
# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Categorize BMI
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}. You are underweight.")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi:.2f}. You are normal.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi:.2f}. You are overweight.")
else:
    print(f"Your BMI is {bmi:.2f}. You are obese.")

#Character type checker  
char = "A"

if char.isalpha():
    print(char, "is an Alphabet")
elif char.isdigit():
    print(char, "is a Digit")
else:
    print(char, "is a Special character")