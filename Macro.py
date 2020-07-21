# define a class that will hold our info about the users daily calories.
# try doing this with the BMR file


class UserMacros:

    # the __init__ function is what you use when you create the object, I have it
    # set up so that if you want to create the 'Macros' object, you have to pass the users
    # daily calories. That number is stored in the object itself. That is where the term
    # 'self.' comes from when you use the class, you are telling Python "I want to use the variable
    # daily_calories found in this class, not some other daily_calories that may have been declared elsewhere"
    def __init__(self, calories):
        self.daily_calories = calories

    # all the functions that belong to your class have 'self' as a parameter.
    # this is mainly just a syntax thing, when you use the function in the
    # main.py you don't need to pass a 'self.' or anything like that, its kinda strange
    def command_prompt(self):
        print("Your daily grams of fat", self.fats_grams())
        print("Your daily grams of protein", self.protein_grams())
        print("Your daily grams of carbohydrates", self.carbohydrates_grams())

    def protein_calories(self):
        return self.daily_calories * .3

    def carbohydrates_calories(self):
        return self.daily_calories * .4

    def fats_calories(self):
        return self.daily_calories * .3

    def protein_grams(self):
        return self.protein_calories() / 4

    def carbohydrates_grams(self):
        return self.carbohydrates_calories() / 4

    def fats_grams(self):
        return self.fats_calories() / 9
