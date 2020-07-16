# imports
import Bmr
import Macro

# main
if __name__ == "__main__":
    height1 = int(input("Enter Height Feet: "))
    height2 = int(input("Enter Height Inches: "))
    weight = int(input("Enter Weight in pounds: "))
    sex = input("Enter Male (M) or Female (F): ").lower().strip()
    age = int(input("Enter Age in years: "))
    inches = (height1 * 12) + height2

    if sex.lower() == 'm':
        print("your basal metabolic rate is", (Bmr.male_bmr()))
        Bmr.male_menu()

    elif sex.lower() == 'f':
        print("Your basal metabolic rate is", (Bmr.female_bmr()))
        Bmr.female_menu()
    else:
        print("enter a valid value m for male f for female")

    # I assume after this first part is where you want to start using all the
    # functions that you created. So if this is the wrong spot you can move it around
    userMacros = Macro.UserMacros(Bmr.male_bmr())
    userMacros.command_prompt()
