# not blank function
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


# dictionary with conversion values for common units
unit_dict={'teaspoon': 5, 'tablespoon': 15,
           'cup': 237,'gram':1,'litre': 1000 ,'ml': 1}

valid = False
while not valid:
    amount = eval(input("How much? "))
    amount = float(amount)

    unit = input("Unit? ")
    if unit in unit_dict:
        multiply_unit = unit_dict.get(unit)
        amount = amount * multiply_unit
        print("Amount in ml {}".format(amount))

    else:
        print("{} is unchanged".format(unit))

