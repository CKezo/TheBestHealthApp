weight = int(input("Your weight: "))
height = int(input("Your height: "))
age = int(input("Your age: "))
gender = int(input("Are you female 1:, or male 2: "))
numberChoice = int(input("Would you like to lose weight 1:, maintain weight 2:, or gain weight 3: "))

formula_1 = 10 * weight + 6.25 * height - 5 * age + 5 #male calories
gainCalories_1 = 400 + formula_1
formula_2 = 10 * weight + 6.25 * height - 5 * age - 161 #female calories
gainCalories_2 = 400 + formula_2

minorDeficit = 10 * weight + 6.25 * height - 5 * age - 250


maintain_1 = 10 * weight + 6.25 * height - 5 * age + 5
maintain_2 = 10 * weight + 6.25 * height - 5 * age - 161

if gender == 1:
    if numberChoice == 1:
        print(f"In order to lose weight, you should eat {minorDeficit} calories per day")
    elif numberChoice == 2:
        print(f"In order to maintain weight, you should eat {maintain_1} calories per day")
    elif numberChoice == 3:
        print(f"In order to gain weight, you should eat {gainCalories_1} calories per day")
elif gender == 2:
    if numberChoice == 1:
        print(f"In order to lose weight, you should eat {minorDeficit} calories per day")
    elif numberChoice == 2:
        print(f"In order to maintain weight, you should eat {maintain_2} calories per day")
    elif numberChoice == 3:
        print(f"In order to gain weight, you should eat {gainCalories_2} calories per day")

