weight = int(input("Your weight: "))
height = int(input("Your height: "))
age = int(input("Your age: "))
gender = input("Are you female or male:")
numberChoice = int(input("Would you like to lose weight 1:, maintain weight 2:, or gain weight 3:"))

formula_1 = 10 * weight + 6.25 * height - 5 * age + 5
gainCalories_1 = 400 + formula_1
formula_2 = 10 * weight + 6.25 * height - 5 * age - 161
gainCalories_2 = 400 + formula_2

minorDeficit = (10*weight) + (6.25*height) - (5*age) - 250
majorDeficit = (10*weight) + (6.25*height) - (5*age) - 500

maintain = 10*weight + 6.25*height - 5*age + 5

if gender.lower() is "male":
    if numberChoice == 1:
        print(f"In order to lose weight, you should eat {minorDeficit} calories per day")
    elif numberChoice == 2:
        print(f"In order to maintain weight, you should eat {maintain} calories per day")
    elif numberChoice == 3:
        print(f"In order to gain weight, you should eat {gainCalories_1} calories per day")
else: 
    if numberChoice == 1:
        print(f"In order to lose weight, you should eat {minorDeficit} calories per day")
    elif numberChoice == 2:
        print(f"In order to maintain weight, you should eat {maintain} calories per day")
    elif numberChoice == 3:
        print(f"In order to gain weight, you should eat {gainCalories_2} calories per day")

