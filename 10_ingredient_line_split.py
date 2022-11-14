import re

full_recipe=[
    "1 1/2 ml flour",
    "3/4 cup milk",
    "1 cup flour",
    "2 tablespoons white sugar",
    "1.5 tsp baking powder",
    "pinch of cinnamon"

]

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

for recipe_line in full_recipe:
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
        get_amount = recipe_line.split(" ", 1)

        try:
            amount = eval(get_amount[0])
        except NameError:
            amount = get_amount[0]
            convert="no"

        unit_ingredient = get_amount[1]

    get_unit = unit_ingredient.split(" ", 1)

    print(amount, unit_ingredient)




