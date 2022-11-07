
def not_blank(question,error):
    valid = False
    while not valid:
        # ask user for entry and assesses if not blank
        response = input(question).strip().lower()
        if response != "":
            return response
            valid = True
        else:
            print(error)


recipe_name = not_blank("What is the name of your recipe?", "This can't be blank" )
recipe_source = not_blank("Where did you get your recipe from?", "This cannot be blank")
