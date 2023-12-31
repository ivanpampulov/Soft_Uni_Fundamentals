import re

names = input()
valid_names = []

regex_pattern = '\\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\\b\\g'
matches = re.findall(regex_pattern, names)

for name in matches:
    if name not in valid_names:
        valid_names.append(name)

    else:
        pass

print(' '.join(valid_names))