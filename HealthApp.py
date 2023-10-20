weight = int(input("Your weight: "))
height = int(input("Your height: "))
age = int(input("Your age: "))

formula = int(10 * weight + 6.25 * height - 5 * age + 5)
calories = 400 + formula
print("To gain weight, you need" ,  calories , "calories per day")

minorDeficit = (10*weight) + (6.25*height) + (5*age) - 250
majorDeficit = (10*weight) + (6.25*height) + (5*age) - 500

maintain = (f"To maintain your current weight, you need to consume {10*weight + 6.25*height - 5*age + 5} calories")
print(maintain)
