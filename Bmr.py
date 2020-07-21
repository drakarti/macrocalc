def male_bmr(weight, inches, age):
    return 66 + (6.2 * weight) + (12.7 * inches) - (6.76 * age)


def female_bmr(weight, inches, age):
    return 655 + (4.3 * weight) + (4.7 * inches) - (4.7 * age)


def maintenance_calories(user_bmr):
    choice = int(input("What is your activity level?\n"
                       "\t1. sedentary\n"
                       "\t2. lightly active\n"
                       "\t3. moderately active\n"
                       "\t4. very active\n "
                       "\t5. extremely active\n"))
    if choice == 1:
        print("Your maintenance calories are", round(user_bmr * 1.2))
    elif choice == 2:
        print("Your maintenance calories are", round(user_bmr * 1.375))
    elif choice == 3:
        print("Your maintenance calories are", round(user_bmr * 1.55))
    elif choice == 4:
        print("Your maintenance calories are", round(user_bmr * 1.725))
    elif choice == 5:
        print("Your maintenance calories are", round(user_bmr * 1.9))
    else:
        print("error")
