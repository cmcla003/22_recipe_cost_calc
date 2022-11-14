import csv

# open file
groceries = open('01_ingredients_ml_to_g.csv')

# read data into list
csv_groceries = csv.reader(groceries)

# convert list to dictionary
food_dict={}

for row in csv_groceries:
    food_dict[row[0]] = row[1]


# check if value in food dictionary
keep_going=""
while keep_going =="":
    amount = eval(input("How much? "))
    amount = float(amount)

    # get ingredient to match to dictionay
    ingredient = input("Ingredient: ").lower().strip()

    if ingredient in food_dict:
        multiply_by = food_dict.get(ingredient)
        amount = amount * float(multiply_by) / 250
        print("Amount in g {}".format(amount))

    else:
        print("{} is unchanged".format(amount))





