weight = int(input("Your weight: "))
height = int(input("Your height: "))
age = int(input("Your age: "))
numberChoice = int(input("Would you like to 1: lose weight, 2: maintain weight, or 3: gain weight?"))

formula = (10 * weight + 6.25 * height - 5 * age + 5)
gainCalories = 400 + formula
#print("To gain weight, you need" ,  calories , "calories per day")

minorDeficit = ((10*weight) + (6.25*height) - (5*age)) - 250
majorDeficit = (10*weight) + (6.25*height) - (5*age) - 500

maintain = 10*weight + 6.25*height - 5*age + 5
#print(maintain)
if numberChoice == 1:
    print(f"In order to lose weight, you should eat {minorDeficit} calories per day")
elif numberChoice == 2:
    print(f"In order to maintain weight, you should eat {maintain} calories per day")
elif numberChoice == 3:
    print(f"In order to gain weight, you should eat {gainCalories} calories per day")