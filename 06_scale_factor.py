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


# main routine
scale_ok = "no"
while scale_ok =="no":
    serving_size = num_check("How many servings is the recipe? ")
    desired_serving = num_check("How many servings are needed? ")

    scale_factor = desired_serving/serving_size

    if scale_factor < 0.25:
        sf_ok = input("""Warning this scale is small,
accurate measurement of ingredients may be hard.
Do you want to keep going? Yes/No""").strip().lower()
    elif scale_factor > 4:
        sf_ok = input("""Warning this scale is large,
be aware you have enough space for all ingredients.
Do you want to keep going? Yes/No""").strip().lower()
    else:
        print("Scale factor: {}".format(scale_factor))

