

def int_check(question,error):

    valid = False
    while not valid:
        try:
            response = int(input(question))

            if response > 0 and response <= 20:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

total_serving = int_check("How many serves does the current recipe make? ","Please enter a max serving of 20 ")
desired_serving = int_check("How many serve of your recipe do you want to make? ", "Please enter a whole number")
print("Total servings: {}".format(total_serving))
print("Desired serving: {}".format(desired_serving))
