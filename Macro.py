from Bmr import male_bmr, female_bmr

daily_calories = male_bmr()


def protein_calories():
    return daily_calories * .3


def carbohydrates_calories():
    return daily_calories * .4


def fats_calories():
    return daily_calories * .3


def protein_grams():
    return protein_calories() / 4


def carbohydrates_grams():
    return carbohydrates_calories() / 4


def fats_grams():
    return fats_calories() / 9


print("Your daily grams of fat", fats_grams())
print("Your daily grams of protein", protein_grams())
print("Your daily grams of carbohydrates", carbohydrates_grams())







