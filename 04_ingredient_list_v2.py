
#not blank and checks for digit user entry
def not_blank(question,number_ok):
    error = "Cannot be blank"
    digi_error = "Cannot have numbers"
    valid = False
    while not valid:
        # ask user for entry and assesses if not blank
        response = input(question).strip().lower()
        has_errors = ""

        if number_ok != "yes":
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        if has_errors != "":
            print(digi_error)
        else:
            return response
            valid = True


ingredient_list=[]

ingredient = ""
while ingredient != "xxx":

    ingredient = not_blank("Please enter the ingredient: ","no")

    if ingredient in ingredient_list:
        print("You have already entered this ingredient, Please enter another")

    if ingredient =="xxx":
        break
    else:
        ingredient_list.append(ingredient)


print(ingredient_list)
