weight = int(input("Your weight: "))
height = int(input("Your height: "))
age = int(input("Your age: "))
gender = int(input("Are you male 1:, or female 2: "))
numberChoice = int(input("Would you like to lose weight 1:, maintain weight 2:, or gain weight 3: "))

formula_1 = 10 * weight + 6.25 * height - 5 * age + 5 #male calories #maintain
minorgainCalories_1 = 250 + formula_1 #gaining minor
majorgainCalories_1 = 500 + formula_1 #gaining major

formula_2 = 10 * weight + 6.25 * height - 5 * age - 161 #female calories #maintain
minorgainCalories_2 = 250 + formula_2 #gaining minor 
majorgainCalories_2 = 500 + formula_2 #gaining major


minorDeficit_1 = formula_1 - 250 #minordeficit male
majorDeficit_1 = formula_1 - 500 #majordeficit male 

minorDeficit_2 = formula_2 - 250 #minordeficit female
majorDeficit_2 = formula_2 - 500 #majordeficit female



if gender == 1:
    if numberChoice == 1:
            print(f"In order to lose weight, you should eat {minorDeficit_1} calories per day")
        elif numberChoice == 2:
            print(f"In order to maintain weight, you should eat {formula_1} calories per day")
        elif numberChoice == 3:
            print(f"In order to gain weight, you should eat {gainCalories_1} calories per day")
elif gender == 2:
    if numberChoice == 1:
        print(f"In order to lose weight, you should eat {minorDeficit} calories per day")
    elif numberChoice == 2:
        print(f"In order to maintain weight, you should eat {formula_2} calories per day")
    elif numberChoice == 3:
        print(f"In order to gain weight, you should eat {gainCalories_2} calories per day")

