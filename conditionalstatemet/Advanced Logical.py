#Triangle 
    # Get user input
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

# Check if sides can form a triangle
if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    print("These sides can form a triangle.")
else:
    print("These sides cannot form a triangle.")

#Calculate tax based on salary  
salary = 6000000
if salary <= 5000000:
    tax = salary * 0.05
    print("Tax:", tax)
elif salary > 5000000 and salary <= 10000000:
    tax = salary * 0.10
    print("Tax:", tax)
else:
    tax = salary * 0.20
    print("Tax:", tax)

# Categorize age  
age = 35
if age >= 0 and age <= 12:
    print("You are a Child")
elif age >= 13 and age <= 19:
    print("You are a Teen")
elif age >= 20 and age <= 59:
    print("You are an Adult")
else:
    print("You are a Senior")



#Logical AND check  
num = 20
if num > 10 and num % 2 == 0:
    print(num, "is greater than 10 and divisible by 2")
else:
    print(num, "does not meet the conditions")


#Logical OR check
num = 3
if num < 5 or num > 20:
    print(num, "meets the condition")
else:
    print(num, "does not meet the condition")