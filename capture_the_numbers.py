import re

lines = input()
my_list = []

while lines:

    pattern = r'\d+'
    matches = re.findall(pattern, lines)
    if matches is None:
        pass
    else:
        my_list += matches

    lines = input()

print(' '.join(my_list))