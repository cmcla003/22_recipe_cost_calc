import re

recipe_line= input("Ingredient: ")

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"


recipe_line = recipe_line.strip()
if re.match(mixed_regex,recipe_line):

    # get mixed number by matching to regex
    pre_mixed_num = re.match(mixed_regex, recipe_line)
    mixed_num = pre_mixed_num.group()

    # change amount to a decimal
    amount= mixed_num.replace(" ","+")
    amount = eval(amount)

    # get unit and ingredient
    compile_regex = re.compile(mixed_regex)

    unit_ingredient = re.split(compile_regex,recipe_line)
    unit_ingredient = (unit_ingredient[1]).strip()

else:
    # allows for units is pinch/dash
    get_amount = recipe_line.split(" ", 1)
    try:
        amount = eval(get_amount[0])
    except NameError:
        amount = get_amount[0]
        convert="no"

    unit_ingredient = get_amount[1]

get_unit = unit_ingredient.split(" ", 1)

# get uni and ingredient name
unit= get_unit[0]
ingredient = get_unit[1]






