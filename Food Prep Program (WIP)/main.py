# --------------------------------------------------------------------------------
# Name: Nicholas Colvin
# Abstract: This program automatically generates weekly meal plans!
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# Imports – built-in and external libraries
# --------------------------------------------------------------------------------
import random
import os
# import math
# import datetime

# --------------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------------
astrDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
strMealFile = "meals.txt"


# --------------------------------------------------------------------------------
# Class Level Varables
# --------------------------------------------------------------------------------
astrCatagoryData = []
astrCookTime = []
astrMealName = []



# --------------------------------------------------------------------------------
# Name: ValidateInteger
# Abstract: Vaildates postive integer inputs
# --------------------------------------------------------------------------------
def ValidateInteger(strInputMessage):
    while True:
        try:
            intInput = input(strInputMessage)

            intInput = int(intInput)
            if intInput > 0:
                return intInput
            else:
                print("INVALID: Please enter a number greater than 0")

        except ValueError:
            print("INVALID: Please enter a number ")



# --------------------------------------------------------------------------------
# Name: LoadMeals
# Abstract: Load meal data
# --------------------------------------------------------------------------------
def LoadMeals():
    global astrCatagoryData, astrCookTime, astrMealName
    
    # Reset Data
    astrCatagoryData = []
    astrCookTime = []
    astrMealName = []
    # Does the file not exist?
    if not os.path.exists(strMealFile):
        # Yes, Generate file
        clsFile = open(strMealFile, 'a')
        clsFile.close()
    
    clsFile = open(strMealFile, 'r')

    #Loop through text file line by line
    for strLine in clsFile:
        # Trim whitespace & find indexes
        strLine = strLine.strip()
        intFirstPipeIndex = strLine.find('|')
        intSecondPipeIndex = strLine.find('|', intFirstPipeIndex + 1)

        # Extract and appended data into arrays
        astrCatagoryData.append(strLine[:intFirstPipeIndex])
        astrCookTime.append(strLine[intFirstPipeIndex + 1:intSecondPipeIndex])
        astrMealName.append(strLine[intSecondPipeIndex + 1:])

    clsFile.close()



# --------------------------------------------------------------------------------
# Name: AddMeals
# Abstract: Add a meal
# --------------------------------------------------------------------------------
def AddMeals():
    while True:
        print("---New Meal---------\n")
        strMealName = input("Enter a meal name : ")
        strCatagory = InputCatagory()
        intCookTime = ValidateInteger("Enter an average cook time : ")
        
        strNewMeal = f"{strCatagory}|{intCookTime}|{strMealName}"
        SaveMeal(strNewMeal)

        intUserInput = BackToMain("1) Another Meal?")
        if intUserInput == 2:
            break 



# --------------------------------------------------------------------------------
# Name: InputCatagory
# Abstract: Add a Catagory (AddMeal Helper function)
# --------------------------------------------------------------------------------
def InputCatagory():
    intUserInput = 0;
    strCatagory = ""
    while True:
        print("1) Rice Dish")
        print("2) Pasta Dish")
        print("3) Casserole")
        print("4) Breakfast")
        print("5) Soup/Stew")
        print("6) Oven Dish")
        print("7) One-pot Dish");
        intUserInput = ValidateInteger("Please select a catagory: ");
        if intUserInput == 1:
            strCatagory = "Rice Dish"
        elif intUserInput == 2:
            strCatagory = "Pasta Dish"
        elif intUserInput == 3:
            strCatagory = "Casserole"
        elif intUserInput == 4:
            strCatagory = "Breakfast"
        elif intUserInput == 5:
            strCatagory = "Soup/Stew"
        elif intUserInput == 6:
            strCatagory = "Oven Dish"
        elif intUserInput == 7:
            strCatagory = "One-pot Dish"
        else:
            print("Invalid: Pick a number 1-7")

        if intUserInput < 8:
            break

    return strCatagory



# --------------------------------------------------------------------------------
# Name: SaveMeal
# Abstract: Save a meal to meal.txt
# --------------------------------------------------------------------------------
def SaveMeal(strNewMeal):
    clsFile = open(strMealFile, 'a')
    clsFile.write(strNewMeal.strip() + "\n")
    clsFile.close()



# --------------------------------------------------------------------------------
# Name: BackToMain
# Abstract: Ask the user to repeat or return to the main menu
# --------------------------------------------------------------------------------
def BackToMain(strMessage):
    # Loop until a valid input is found
    while True:
        print(strMessage)
        print("2) Back to main menu")
        
        # Validate 
        intUserInput = ValidateInteger("Please enter a number: ")
        
        # In Range?
        if intUserInput == 1 or intUserInput == 2:
            # Yes, return input
            break
        else:
            # No, display and loop
            print("INVALID: Please enter 1 or 2")
    
    return intUserInput



# --------------------------------------------------------------------------------
# Name: RemoveMeals
# Abstract: Remove meals
# --------------------------------------------------------------------------------
def RemoveMeals():
    intIndex = int(0)
    intMealIndex = 0
    intUserInput = 0

    while True:
        # Load Meals
        LoadMeals();

        if len(astrMealName) > 0:
            # Display all meals
            for strMeal in astrMealName:
                intIndex += 1
                print(intIndex, ")", strMeal)
            # Get user input
            intMealIndex = ValidateInteger("Please select a meal to remove: ")
            
            # In Range? 
            if intUserInput <= intIndex:
                # Yes, delete meal
                DeleteMeal(intMealIndex)
                # Refresh Data
                LoadMeals();
            else:
                # No, 
                print("INVALID: Please enter a number within range")
            
            # Get user input
            intUserInput = BackToMain("1) Remove another meal")
            
            # Return to main?
            if intUserInput == 2:
                # Yes, break
                break
        else:
            print("ERROR: No meals found. Please enter some meals!")
            break


# --------------------------------------------------------------------------------
# Name: DeleteMeal
# Abstract: Delete a meal from meals.txt
# --------------------------------------------------------------------------------
def DeleteMeal(intUserInput):
    intIndex = 1;
    clsFile = open(strMealFile,"r")
    strLines = clsFile.readlines()
    clsFile.close()

    clsFile = open(strMealFile, "w")
    

    for strLine in strLines:
        if intIndex != intUserInput:
            clsFile.write(strLine)
        intIndex += 1
    
    clsFile.close()



# --------------------------------------------------------------------------------
# Name: main
# Abstract: This is where the program starts
# --------------------------------------------------------------------------------
intUserInput = int(0);
while True:
    print("1) Create Meal Plan");
    print("2) Add Meals");
    print("3) Remove Meals");
    print("4) Exit");
    # Vaildate
    intUserInput = ValidateInteger("Please enter a number: ");
    
    # Options
    if intUserInput == 1:
        CreateMealPlan();
    elif intUserInput == 2:
        AddMeals();
    elif intUserInput == 3:
        RemoveMeals();
    elif intUserInput == 4:
        break
    else: print("Input Invalid")