import re

recipe_line="1 1/2 ml flour"

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

if re.match(mixed_regex,recipe_line):
    print("true")
else:
    print("false")
