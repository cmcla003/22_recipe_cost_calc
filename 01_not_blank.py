
def not_blank(question):
    valid = False
    while not valid:
        # ask user for entry and assesses if not blank
        response = input(question).strip().lower()
        if response.isdigit():
            print("Entry cannot have numbers please try again")
            valid = False
        elif response != "":
            return response
            valid = True

        else:
            print("Entry cannot be blank")


recipe_name = not_blank("What is the name of your recipe?")
recipe_source = not_blank("Where did you get your recipe from?")

print("You chose {} from {}".format(recipe_name,recipe_source))
