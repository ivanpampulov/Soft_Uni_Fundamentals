import re

items_bought = []
total_spend = 0

while True:
    lines = input()

    if lines == 'Purchase':
        break

    pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
    matches = re.finditer(pattern, lines)

    for match in matches:
        item = match.group(1)
        price = match.group(2)
        quantity = match.group(3)

        items_bought.append(item)
        money_spend = float(price) * int(quantity)
        total_spend += money_spend

print('Bought furniture:')

for i in range(len(items_bought)):
    print(f'{items_bought[i]}')

print(f'Total money spend: {total_spend:.2f}')


