def male_bmr(weight, inches, age):
    return 66 + (6.2 * weight) + (12.7 * inches) - (6.76 * age)


def female_bmr(weight, inches, age):
    return 655 + (4.3 * weight) + (4.7 * inches) - (4.7 * age)


def male_menu():
    print("What is your activity level?, \n"
          "\t1. sedentary\n"
          "\t2. lightly active\n"
          "\t3. moderately active\n"
          "\t4. very active\n "
          "\t5. extremely active\n")
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
    print("What is your activity level?,\n"
          "\t1. sedentary\n"
          "\t2. lightly active\n"
          "\t3. moderately active\n"
          "\t4. very active\n "
          "\t5. extremely active\n")
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