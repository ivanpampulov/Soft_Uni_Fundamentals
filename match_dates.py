import re

dates = input()

pattern = r'(\d{2})([./-])([A-Z][a-z]{2})\2(\d{4})'
match = re.finditer(pattern, dates)

for i in match:
    day = i.group(1)
    month = i.group(3)
    year = i.group(4)

    print(f'Day: {day}, Month: {month}, Year: {year}')
