import csv
import os
import itertools

#Note that this program strictly takes into account the number of calories burned from physical activity in addition to user stats and does not account for
#long term raised metabolism changes which would mean your daily caloric intake would be higher than this tool would suggest

# Get the directory of this Python file which is where the csv doc should also be saved.
script_dir = os.path.dirname(os.path.abspath(__file__))

# Sets the working directory to the location above. Needed to ensure the csv file path below can be found on different teammate's computers.
os.chdir(script_dir)

exerciseCSV = "Exercise.csv"

def printActivities(filepath): #This shows the user all the major categories of physical activities to choose from
    with open(filepath, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        for row in csv_reader:
            if row[0].strip() and all(not cell.strip() for cell in row[1:]):
              print(row[0])

def userHasChosenValidActivity(filepath):
    with open(filepath, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        foundMatchingActivity = False

        for row in csv_reader:
            if row[0].strip() and all(not cell.strip() for cell in row[1:]) and (row[0].lower() == preferredActivity.lower()):
              foundMatchingActivity = True
        
        if foundMatchingActivity == False:
            print("Sorry, the activity you entered is either mispelled or not in our catalogue")
            return foundMatchingActivity
        return foundMatchingActivity


def selectActivityOptionAndReturnCaloriesBurned(filepath):
    startRowNum = 0
    endRowNum = 0
    foundStartRow = False

    with open(filepath, 'r') as csvfile: #this section finds the index of the rows of specific activities we want to show our user
        csv_reader = csv.reader(csvfile)
        for rowNum, row in enumerate(csv_reader, start=1):
            if foundStartRow == False:       #Not really necessary in such a small program but in a larger program, wouldn't want to expend extra computing power on the statement immediately below once we have the necessary info so just practicing for such scenarios.
                if row[0].strip() and all(not cell.strip() for cell in row[1:]) and (row[0].lower() == preferredActivity.lower()):
                    startRowNum = rowNum
                    foundStartRow = True
                    continue
            if foundStartRow == True:
                if row[0].strip() and all(not cell.strip() for cell in row[1:]) and startRowNum != 0:
                    endRowNum = rowNum - 1
                    break
    
    activityNum = 1
    #Have to re-open the csv otherwise it will continue iterating where it left off in previous for loop
    with open(filepath, 'r') as csvfile: #This section prints out the activities for user selection
        csv_reader = csv.reader(csvfile)
        for row in itertools.islice(csv_reader, startRowNum, endRowNum):
            print(f"{activityNum}: {row[0]}")
            activityNum = activityNum + 1
    
    userActivityOption = int(input("Please enter the number of your preferred choice of the options above: "))
    while True:
        try:
            if 0 < userActivityOption < activityNum:
                break
            else:
                userActivityOption = int(input("Sorry, please select a number from the options above: "))
        except ValueError:
            print("Invalid input. Please enter a number")

    with open(filepath, 'r') as csvfile: #confirms user selection and returns a list of calorie burned values to be used to later calcuate exact calories burned for a user's given weight
        csv_reader = csv.reader(csvfile)
        targetRow = startRowNum + userActivityOption - 1
        for row in itertools.islice(csv_reader, targetRow, targetRow + 1):
            print(f"You selected: {row[0]}")
            calorieList = [int(cell) for cell in row[1:5]]
            return calorieList
            
#The data we used for our program only lists calorie data points for 4 different weights so the function below uses linear regression to extrapolate what the calories burned would be based on user-inputted weight that likely does not match the 4 values we had to work from.
def activityCalorieCalculator(weightList, calorieList, userWeight):
    meanWeight = sum(weightList)/len(weightList)
    meanCals = sum(calorieList)/len(calorieList)

    numerator = sum((weightList[i] - meanWeight) * (calorieList[i] - meanCals) for i in range(len(weightList)))
    denominator = sum((weightList[i] - meanWeight) ** 2 for i in range(len(weightList)))
    b = numerator/denominator
    a = meanCals - b * meanWeight
    caloriesBurnedForGivenWeight = b * userWeight + a
    return caloriesBurnedForGivenWeight

print("So you wanna get your weight on point, huh? Simply give us some info below and leave all that horrible number-crunching to us, dear valuable user.")
weight = int(input("Your weight in kilograms: "))
height = int(input("Your height in centimeters: "))
age = int(input("Your age: "))
gender = int(input("Are you 1: female, or 2: male: "))
weightGoal = int(input("Would you like to 1: lose weight, 2: maintain weight, or 3: gain weight: "))

#"formula" vars below using Mifflin-St Jeor Equation
maleFormula = 10 * weight + 6.25 * height - 5 * age + 5
maleGainCalories = maleFormula + 400
maleDeficit = maleFormula - 250
femaleFormula = 10 * weight + 6.25 * height - 5 * age - 161
femaleGainCalories = femaleFormula + 400
femaleDeficit = femaleFormula - 250

print("Would you like to incorporate exercise into your calculations? Yes or No")
exerciseIncluded = False
while True:
    userChoice = input()
    if userChoice.lower() == "yes":
        exerciseIncluded = True
        break
    elif userChoice.lower() == "no":
        exerciseIncluded == False
        break
    else:
        print("Invalid answer. Please enter 'Yes' or 'No'")


weightList = []
calorieList = []
caloriesBurnedPerDay = 0
caloriesBurnedPerHour = 0

if exerciseIncluded:
    printActivities(exerciseCSV)
    preferredActivity = input("What type of activty do you enjoy? ")
    while not userHasChosenValidActivity(exerciseCSV):
        preferredActivity = input("Please enter your preferred activity again: ")

    weightList = [59, 70, 82, 93]
    calorieList = selectActivityOptionAndReturnCaloriesBurned(exerciseCSV)
    caloriesBurnedPerHour = activityCalorieCalculator(weightList, calorieList, weight)
    print("On average, about how many minutes per day do you plan to do this activity?")
    userMinutes = 0
    while True:
        try:
            userMinutes = int(input())
            if userMinutes < 0 or userMinutes > 1440:
                print("Please enter a valid amount of real time minutes contained within a typical human day")
            else:
                break
        except ValueError:
            print("Please enter a number.")
    caloriesBurnedPerDay = (caloriesBurnedPerHour/60) * userMinutes

if gender == 1:
    if exerciseIncluded:
        if weightGoal == 1:
            print(f"In order to lose weight at a steady pace, you should eat no more than {femaleDeficit + caloriesBurnedPerDay} calories per day")
        elif weightGoal == 2:
            print(f"In order to maintain weight, you should eat {femaleFormula + caloriesBurnedPerDay} calories per day")
        elif weightGoal == 3:
            print(f"In order to gain weight, you should eat {femaleGainCalories + caloriesBurnedPerDay} calories per day")
    else:
        if weightGoal == 1:
            print(f"In order to lose weight at a steady pace, you should eat no more {femaleDeficit} calories per day")
        elif weightGoal == 2:
            print(f"In order to maintain weight, you should eat {femaleFormula} calories per day")
        elif weightGoal == 3:
            print(f"In order to gain weight, you should eat {femaleGainCalories} calories per day")
elif gender == 2:
    if exerciseIncluded:
        if weightGoal == 1:
            print(f"In order to lose weight at a steady pace, you should eat {maleDeficit + caloriesBurnedPerDay} calories per day")
        elif weightGoal == 2:
            print(f"In order to maintain weight, you should eat {maleFormula + caloriesBurnedPerDay} calories per day")
        elif weightGoal == 3:
            print(f"In order to gain weight, you should eat {maleGainCalories + caloriesBurnedPerDay} calories per day")
    else:
        if weightGoal == 1:
            print(f"In order to lose weight at a steady pace, you should eat {maleDeficit} calories per day")
        elif weightGoal == 2:
            print(f"In order to maintain weight, you should eat {maleFormula} calories per day")
        elif weightGoal == 3:
            print(f"In order to gain weight, you should eat {maleGainCalories} calories per day")


#Ideas for things to add:
#User input validation for all user input variables
#Losing/gaining weight at faster paces calculation
#Handling extreme cases - for example, if you put in very low weight and height and exercise a lot, the tool will tell you to eat negative calories
#Calculating the rate at which the user will lose weight per week/month
#Ask user if they prefer imperial or metric system and create height/weight variables based on the response. Program runs on metric variables so conversion from imperial would be needed.