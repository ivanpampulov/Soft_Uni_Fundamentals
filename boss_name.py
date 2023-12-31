import re

number_of_inputs = int(input())

for i in range(number_of_inputs):
    command = input()

    pattern = r'^\|([A-Z]+)\|:#([A-Za-z]+ [A-Za-z]+)#$'
    matches = re.finditer(pattern, command)

    if re.search(pattern, command) is None:
        print('Access denied!')

    for match in matches:
        boss_name = match.group(1)
        title = match.group(2)
        print(f'{boss_name}, The {title}')
        print(f'>> Strength: {len(boss_name)}')
        print(f'>> Armor: {len(title)}')

