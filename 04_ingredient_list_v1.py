def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()

        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response= "no"
            return response
        else:
            print("Please enter yes or no")

# set up list
ingredient_list = []
# loop ingredient ask until exit code
ready = input("Are you ready to enter your ingredients? ")
if ready == "yes":
    ingredient =""
    while ingredient != "xxx":

        ingredient = input("Please enter the ingredient: ").strip().lower()
        if ingredient == "xxx":
            if len(ingredient_list) <= 1:
                print("Please enter more than 1 ingredient")

        if ingredient in ingredient_list:
            print("You have already entered this ingredient, Please enter another")

        elif ingredient !="xxx":
            ingredient_list.append(ingredient)


print(ingredient_list)
