# --------------------------------------------------------------------------------
# Name: Nicholas Colvin
# Abstract: This program automatically generates weekly meal plans!
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# Imports – built-in and external libraries
# --------------------------------------------------------------------------------
import random
import os
from datetime import datetime 
from datetime import timedelta
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
# import math

# --------------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------------
astrDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
strMealFile = "meals.txt"
# --------------------------------------------------------------------------------
# Class Level Varables
# --------------------------------------------------------------------------------
adctMeals = [] 


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
# Name: InputCookType 
# Abstract: Add a Cook Type (AddMeal Helper function)
# --------------------------------------------------------------------------------
def InputCookType():
    intUserInput = 0;
    strCookType = ""
    dish_types = {
    1: "Rice",
    2: "Pasta",
    3: "Casserole",
    4: "Crockpot",
    5: "Oven",
    6: "Stovetop"
    }

    while True:
        print("1) Rice")
        print("2) Pasta")
        print("3) Casserole")
        print("4) Crockpot")
        print("5) Oven")
        print("6) Stovetop");
        intUserInput = ValidateInteger("Please select a catagory: ");

        if intUserInput > 6:
            print("INVALID: Please select a valid catagory")
        else:
            strCookType = dish_types.get(intUserInput)
            break


    return strCookType
    


# --------------------------------------------------------------------------------
# Name: InputCatagory
# Abstract: Add a Cook Type (AddMeal Helper function)
# --------------------------------------------------------------------------------
def InputCatagory():
    intUserInput = 0;
    strCatagory = ""
    strCatagoryList = {
    1: "Italian",
    2: "Mexican",
    3: "American",
    4: "Indian",
    5: "Thai",
    6: "Spanish"
    }

    while True:
        print("1) Italian")
        print("2) Mexican")
        print("3) American")
        print("4) Indian")
        print("5) Thai")
        print("6) Spanish");
        intUserInput = ValidateInteger("Please select a catagory: ");

        if intUserInput > 6:
            print("INVALID: Please select a valid catagory")
        else:
            strCatagory = strCatagoryList.get(intUserInput)
            break


    return strCatagory



# --------------------------------------------------------------------------------
# Name: AddMeals
# Abstract: Add a meal
# --------------------------------------------------------------------------------
def AddMeals():
    while True:
        print("---New Meal---------\n")
        strMealName = input("Enter a meal name : ")
        strCatagory = InputCatagory()
        strCookType = InputCookType()
        intPrepTime = ValidateInteger("Enter an average prep time (in minutes) : ")
       
        strNewMeal = f"{strCatagory}|{strCookType}|{intPrepTime}|{strMealName}"
        SaveMeal(strNewMeal, strMealFile)

        intUserInput = BackToMain("1) Another Meal?")
        if intUserInput == 2:
            break 



# --------------------------------------------------------------------------------
# Name: MondayFilter
# Abstract: Return true if the Monday condition is met
# --------------------------------------------------------------------------------
def MondayFilter(dctMeal):
    blnFlag = False

    if dctMeal["cook-type"] == "Crockpot":
        blnFlag = True

    return blnFlag
    


# --------------------------------------------------------------------------------
# Name: TuesdayFilter
# Abstract: Return true if the Tuesday condition is met
# --------------------------------------------------------------------------------
# def TuesdayFilter(dctMeal):
#     blnFlag = False

#     if dctMeal["cook-type"] == "crockpot":
#         blnFlag == True

#     return blnFlag
    


# --------------------------------------------------------------------------------
# Name: WednesdayFilter
# Abstract: Return true if the Wednesday condition is met
# --------------------------------------------------------------------------------
def WednesdayFilter(dctMeal):
    blnFlag = False

    if dctMeal["cook-type"] == "Rice":
        blnFlag = True

    return blnFlag
    


# --------------------------------------------------------------------------------
# Name: ThursdayFilter
# Abstract: Return true if the Thursday condition is met
# --------------------------------------------------------------------------------
def ThursdayFilter(dctMeal):
    blnFlag = False

    if dctMeal["cook-type"] == "Pasta":
        blnFlag = True

    return blnFlag
    


# --------------------------------------------------------------------------------
# Name: FridayFilter 
# Abstract: Return true if the Monday condition is met
# --------------------------------------------------------------------------------
# def MondayFilter(dctMeal):
#     blnFlag = False

#     if dctMeal["cook-type"] == "crockpot":
#         blnFlag == True

#     return blnFlag
    


# --------------------------------------------------------------------------------
# Name: SaturdayFilter
# Abstract: Return true 
# --------------------------------------------------------------------------------
def SaturdayFilter(dctMeal):
    return True


    
# --------------------------------------------------------------------------------
# Name: SundayFitler 
# Abstract: Return true if the Monday condition is met
# --------------------------------------------------------------------------------
def SundayFilter(dctMeal):
    return True
    


# --------------------------------------------------------------------------------
# Name: GetFileName
# Abstract: Format and return the File Name
# --------------------------------------------------------------------------------
def GetFileName():
    strCurrentDate = datetime.now()
    strNextWeek = strCurrentDate + timedelta(days=7)

    strFileName = f"Meal Plan {strCurrentDate.strftime('%B')} {strCurrentDate.day} - {strNextWeek.strftime('%B')} {strNextWeek.day}"
    print (strFileName)
    return strFileName



# --------------------------------------------------------------------------------
# Name: SaveMealPlan
# Abstract: Save most recent entries to avoid geting the same meals next week.
# --------------------------------------------------------------------------------
def SaveMealPlan(adctMealPlan ,strFileName="previous-meal-plan.txt"):
    if not os.path.exists(strFileName):
        # Yes, Generate file
        clsFile = open(strFileName, 'a')
        clsFile.close()

    clsFile = open(strFileName, 'r')
    adctMealValues = adctMealPlan.values()
    for dctMeal in adctMealValues:
        if isinstance(dctMeal, dict):
            strMealName = dctMeal.get("name")
        else:
            strMealName = str(dctMeal) 
        
        SaveMeal(strMealName, strFileName)

    

 # --------------------------------------------------------------------------------
# Name: GetEligibleMeals
# Abstract: Generate a list of possiable meals to choose from
# --------------------------------------------------------------------------------  
def GetEligibleMeals(FilterFunction, aUsedMeals):
    astrEligibleMeals = []               
    for dctMeal in adctMeals:
        strMealName = dctMeal.get("name", "")
        if FilterFunction(dctMeal) == True and strMealName not in aUsedMeals:
            astrEligibleMeals.append(dctMeal)
    return astrEligibleMeals



 # --------------------------------------------------------------------------------
# Name: GetMealForDay
# Abstract: Generate meal for the current day
# --------------------------------------------------------------------------------  
def GetMealForDay(strDay, aUsedMeals):
    adctDayFilters = {
        "Monday": MondayFilter,
        "Wednesday": WednesdayFilter,
        "Thursday": ThursdayFilter,
        "Saturday": SaturdayFilter,
        "Sunday": SundayFilter
    }
    if strDay not in adctDayFilters:
        return f"No Filter Found for {strDay}"
    
    CurrentFilter = adctDayFilters[strDay]
    
    astrEligibleMeals = GetEligibleMeals(CurrentFilter, aUsedMeals)

    if not astrEligibleMeals:
        return f"No Meal Found for {strDay}"

    dctChosenMeal = random.choice(astrEligibleMeals)
    strMealName = dctChosenMeal.get("name", "UnamedMeal")
    aUsedMeals.add(strMealName)

    return dctChosenMeal
    


# --------------------------------------------------------------------------------
# Name: LoadPreviousMeals
# Abstract: Load the most recently used meals to the blocklist
# --------------------------------------------------------------------------------
def LoadPreviousMeals(strFileName="previous-meal-plan.txt"):
    aUsedMeals = set()
    if os.path.exists(strFileName):
        clsFile = open(strFileName, "r")
        for strLine in clsFile:
            strMealName = strLine.strip()
            if strMealName:
                aUsedMeals.add(strMealName)
        clsFile.close()

        clsFile = open(strFileName, "w")
        clsFile.close()


    return aUsedMeals


# --------------------------------------------------------------------------------
# Name: GetMealsForMealPlan
# Abstract: Generate a list of meals for the week!
# --------------------------------------------------------------------------------
def GetMealsForMealPlan():
    global adctMeals, astrDays
    
    LoadMeals()
    adctMealPlan = {}
    aUsedMeals = LoadPreviousMeals()
    
    for strDay in astrDays:
        if strDay == "Tuesday":
            adctMealPlan[strDay] = "Eat-out Night"        
        elif strDay == "Friday":
            adctMealPlan[strDay] = "Grill-Out-Night"
        else: 
            adctMealPlan[strDay] = GetMealForDay(strDay, aUsedMeals);

    SaveMealPlan(adctMealPlan)
    return adctMealPlan
            


# --------------------------------------------------------------------------------
# Name: GenerateMealPlan
# Abstract: Generate a meal plan!
# --------------------------------------------------------------------------------
def GenerateMealPlan():
    adctMealList = GetMealsForMealPlan();           
    strFileName = GetFileName();
    objCanvas = canvas.Canvas(f"Meal-Plans/{strFileName}.pdf", pagesize=letter)
    # Get Pdf's width and height,
    dblMaxWidth, dblMaxHeight = letter 
    dblNewLine = 25
    dblMargin =  52.00
    dblCurrentWidth = dblMargin
    dblCurrentHeight = dblMaxHeight - dblMargin 
    strFontNormal = "Times-Roman"
    strFontBold = "Times-Bold"
    intIndex = 0;
    # Set Header Font
    objCanvas.setFont(strFontBold, 20)
    # Draw Header
    objCanvas.drawString(dblCurrentWidth, dblCurrentHeight, strFileName)
    
    for intIndex in range(7):
        # Get current day and dictionary
        strCurrentDay = astrDays[intIndex]
        dctMeal = adctMealList.get(strCurrentDay)
        # Get Meal Name 
        if isinstance(dctMeal, dict):
            strMealName = dctMeal.get("name")
        else:
            strMealName = str(dctMeal)
        
        # Draw Data onto PDF
        objCanvas.setFont(strFontBold, 14)
        dblCurrentHeight -= dblNewLine
        dblStringWidth = objCanvas.stringWidth(astrDays[intIndex], strFontBold, 14)
        objCanvas.drawString(dblCurrentWidth, dblCurrentHeight, astrDays[intIndex])
        objCanvas.line(dblCurrentWidth, dblCurrentHeight - 2, dblCurrentWidth + dblStringWidth, dblCurrentHeight - 2)
        objCanvas.setFont(strFontNormal, 14)
        objCanvas.drawRightString(450, dblCurrentHeight, "Cooking:________________________")
        dblCurrentHeight -= dblNewLine
        objCanvas.drawString(dblCurrentWidth, dblCurrentHeight, strMealName) 
    objCanvas.save()

    print("Meal Plan Created! Check 'Meal-Plans' folder")




# --------------------------------------------------------------------------------
# Name: SaveMeal
# Abstract: Save a meal to meal.txt
# --------------------------------------------------------------------------------
def SaveMeal(strMeal, strFileName):
    clsFile = open(strFileName, 'a')
    clsFile.write(strMeal.strip() + "\n")
    clsFile.close()



# --------------------------------------------------------------------------------
# Name: LoadMeals
# Abstract: Load meal data
# --------------------------------------------------------------------------------
def LoadMeals():
    global adctMeals    
    # Does the file not exist?
    if not os.path.exists(strMealFile):
        # Yes, Generate file
        clsFile = open(strMealFile, 'a')
        clsFile.close()

    # Open file in read only mode  
    clsFile = open(strMealFile, 'r')

    #Loop through text file line by line
    for strLine in clsFile:
        # Trim whitespace & find split apart data
        strLine = strLine.strip()
        astrParts = strLine.strip().split("|")
        # Four Entries?
        if len(astrParts) == 4:
           # Yes Store data into the specifed catagories
           dctMeal = {
                "catagory": astrParts[0],
                "cook-type": astrParts[1],
                "prep-time": astrParts[2],
                "name": astrParts[3],
           } 
        adctMeals.append(dctMeal)
    # Close File 
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
        GenerateMealPlan();
    elif intUserInput == 2:
        AddMeals();
    elif intUserInput == 3:
        RemoveMeals();
    elif intUserInput == 4:
        break
    else: print("Input Invalid")