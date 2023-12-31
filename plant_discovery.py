import re

number_plants = int(input())
plants_dict = {}

for i in range(number_plants):
    plant, rarity = input().split('<->')

    plants_dict[plant] = [int(rarity), 0, 0]

while True:
    command = input()

    if command == 'Exhibition':
        break

    pattern = r'\w+'
    if command.startswith('Rate') or command.startswith('Update'):
        do, plant, rate = re.findall(pattern, command)
    else:
        do, plant = re.findall(pattern, command)

    if plant not in plants_dict:
        print('error')
        continue

    if do == 'Rate':
        plants_dict[plant][1] += int(rate)
        plants_dict[plant][2] += 1

    elif do == 'Update':
        plants_dict[plant][0] = int(rate)

    elif do == 'Reset':
        plants_dict[plant][1] = 0

print('Plants for the exhibition:')

for key, value in plants_dict.items():

    if value[1] == 0:
        print(f'- {key}; Rarity: {value[0]}; Rating: 0.00')

    else:
        print(f'- {key}; Rarity: {value[0]}; Rating: {value[1]/value[2]:.2f}')







