import re

destination = input()
total_points = 0

pattern = r'(?<=\=)[A-Z][A-Za-z]{2,}(?=\=)|(?<=\/)[A-Z][A-Za-z]{2,}(?=\/)'
matches = re.findall(pattern, destination)

for i in matches:
    points = len(i)
    total_points += points

print(f'Destinations: {", ".join(matches)}')
print(f'Travel Points: {total_points}')


