weight = int(input("Enter your weight: "))
height = int(input("Enter your Heigh in cm: "))
result = weight/((height/100**2))
print(f"Your BMI is: {result:.2f}")
if result <= 18:
    print("You are underweight :(")
elif 18 < result <= 25.5:
    print("You have a healthy weight <3")
elif 25.5 < result <= 30:
    print("You are overweight :(")
else:
    print("You are Obese :(")