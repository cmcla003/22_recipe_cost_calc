# not blank and checks for digit user entry
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
# number check
def num_check(question):
    error= "Please enter a number more than 0"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

# scale factor to be rpelaced with scale once completed
scale_factor = eval(input("Scale factor: "))

ingredient_list=[]

stop= ""
while stop != "xxx":
    ingredient = not_blank("Please enter the ingredient: ","no")

    if ingredient == "xxx" and len(ingredient_list)>=2:
        break
    elif ingredient == "xxx" and len(ingredient_list)<=1:
        print("Please enter more than 2 ingredients")
    elif ingredient in ingredient_list:
        print("You have already entered this ingredient, Please enter another")
    else:
        amount = num_check("How much? ")
        scaled = amount * scale_factor

        #convert to int if whole number
        if scaled % 1 == 0:
            scaled = round(scaled)
        elif scaled * 10 % 1 == 0:
            scaled ="{:.1f}".format(scaled)
        else:
            scaled = "{:.2f}".format(scaled)

        ingredient_list.append([ingredient,amount,scaled])

# print list unit then ingredient
for item in ingredient_list:
    print(item[2],item[0])
