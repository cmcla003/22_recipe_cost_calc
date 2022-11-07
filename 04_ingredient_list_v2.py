def not_blank(question):
    valid = False
    while not valid:
        # ask user for entry and assesses if not blank
        response = input(question).strip().lower()
        for letter in response:
            if letter.isdigit() == True:
                print("Entry cannot have numbers please try again")

        if response != "":
            return response
            valid = True

        else:
            print("Entry cannot be blank")

ingredient_list=[]

ingredient = ""
while ingredient != "xxx":
    num_ingredients = 0

    ingredient = not_blank("Please enter the ingredient: ").strip().lower()
    num_ingredients +=1

    if ingredient in ingredient_list:
        print("You have already entered this ingredient, Please enter another")

    if ingredient =="xxx":
        break
    else:
        ingredient_list.append(ingredient)


print(ingredient_list)
