
#Check a number
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



#Even or odd
num = 6
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#grader

percentage = 92
if percentage >= 90:
    print("Grade: A")
percentage = 75
if percentage >= 70 and percentage < 90:
    print("Grade: B")
percentage = 55
if percentage >= 50 and percentage < 70:
    print("Grade: C")
percentage = 40
if percentage < 50:
    print("Grade: F")



#divisibility
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")

num = 9
if num % 3 == 0:
    print("Divisible by 3")

num = 10
if num % 5 == 0:
    print("Divisible by 5")

num = 7
if num % 3 != 0 and num % 5 != 0:
    print("Not divisible by either 3 or 5")


#smallest number
num1 = 10
num2 = 20
if num1 < num2:
    print(num1)
else:
    print(num2)

num1 = 25
num2 = 15
if num1 < num2:
    print(num1)
else:
    print(num2)



