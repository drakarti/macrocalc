# imports
import Bmr
from Macro import UserMacros

# main, program starts here
if __name__ == "__main__":
    height1 = int(input("Enter Height Feet: "))
    height2 = int(input("Enter Height Inches: "))
    weight = int(input("Enter Weight in pounds: "))
    sex = input("Enter Male (M) or Female (F): ").lower().strip()
    age = int(input("Enter Age in years: "))
    inches = (height1 * 12) + height2

    # calculate bmr based on sex
    user_bmr = None
    if sex == 'm':
        user_bmr = Bmr.male_bmr(weight, inches, age)
    elif sex == 'f':
        user_bmr = Bmr.male_bmr(weight, inches, age)
    else:
        print("enter a valid value m for male f for female")

    # get maintenance calories
    Bmr.maintenance_calories(user_bmr)

    # I assume after this first part is where you want to start using all the Macros
    # functions that you created. So if this is the wrong spot you can move it around
    userMacros = UserMacros(user_bmr)
    userMacros.command_prompt()
