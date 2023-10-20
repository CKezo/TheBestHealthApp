weight = int(input("Your weight: "))
height = int(input("Your height: "))
age = int(input("Your age: "))

formula = int(10 * weight + 6.25 * height - 5 * age + 5)
calories = 400 + formula
print("To gain weight, you need" ,  calories , "calories per day")

