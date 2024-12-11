#6.Find the largest of three numbers
num1 = 10
num2 = 20
num3 = 30

if num1 >= num2:
    if num1 >= num3:
        print(num1, "is the largest")
    else:
        print(num3, "is the largest")
else:
    if num2 >= num3:
        print(num2, "is the largest")
    else:
        print(num3, "is the largest")


 #7.Check leap year  
year = 2024
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")


#8.temperature check
temperature = 25
if temperature < 15:
    print("Temperature is Cold")
elif temperature >= 15 and temperature <= 30:
    print("Temperature is Warm")
else:
    print("Temperature is Hot")


#9.vowels
char = 'a'
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print(char, "is a vowel")
else:
    print(char, "is a consonant")



#10. Driving eligibility  
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You are eligible to drive")
    else:
        print("You need a valid license to drive")
else:
    print("You must be 18 or older to drive")
