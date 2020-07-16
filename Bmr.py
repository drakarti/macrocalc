def male_bmr():
    return 66 + (6.2 * weight) + (12.7 * inches) - (6.76 * age)


def female_bmr():
    return 655 + (4.3 * weight) + (4.7 * inches) - (4.7 * age)


def male_menu():
    print("What is your activity level?, \n"
          " 1. sedentary \n"
          " 2. lightly active \n"
          " 3. moderately active \n"
          " 4. very active \n "
          "5. extremely active ")
    choice = input()
    if choice == "1":
        print("Your maintenance calories are", round(male_bmr()*1.2))

    if choice == "2":
        print("Your maintenance calories are", round(male_bmr()*1.375))

    if choice == "3":
        print("Your maintenance calories are", round(male_bmr()*1.55))

    if choice == "4":
        print("Your maintenance calories are", round(male_bmr()*1.725))

    if choice == "5":
        print("Your maintenance calories are", round(male_bmr()*1.9))


def female_menu():
    print("What is your activity level?, \n"
          " 1. sedentary \n"
          " 2. lightly active \n"
          " 3. moderately active \n"
          " 4. very active \n "
          "5. extremely active ")
    choice = input()
    if choice == "1":
        print("Your maintenance calories are", (female_bmr()*1.2))

    if choice == "2":
        print("Your maintenance calories are", (male_bmr()*1.375))

    if choice == "3":
        print("Your maintenance calories are", (female_bmr()*1.55))

    if choice == "4":
        print("Your maintenance calories are", (female_bmr()*1.725))

    if choice == "5":
        print("Your maintenance calories are", (female_bmr()*1.9))


if __name__ == "__main__":
    height1 = int(input("Enter Height Feet: "))
    height2 = int(input("Enter Height Inches: "))
    weight = int(input("Enter Weight in pounds: "))
    sex = input("Enter Male (M) or Female (F): ").lower().strip()
    age = int(input("Enter Age in years: "))
    inches = (height1 * 12) + height2

    if sex.lower() == 'm':
        print("your basal metabolic rate is", (male_bmr()))
        male_menu()

    elif sex.lower() == 'f':
        print("Your basal metabolic rate is", (female_bmr()))
        female_menu()
    else:
        print("enter a valid value m for male f for female")
