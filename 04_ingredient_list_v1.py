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

ingredient = ""
while ingredient != "xxx":

    ingredient = input("Please enter the ingredient: ").strip().lower()

    if ingredient in ingredient_list:
        print("You have already entered this ingredient, Please enter another")

    if ingredient != "xxx":
        ingredient_list.append(ingredient)
    else:
        break

print(ingredient_list)
