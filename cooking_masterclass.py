#User input
from math import ceil

budget = float(input())
students = int(input())

flour_price = float(input())
flour_price_total = flour_price * students
egg_price = float(input()) * 10 * students
apron_per_piece = float(input())

apron_total = apron_per_piece * ceil(students * 1.2)
total_cost = flour_price_total + egg_price + apron_total


for i in range(1, students + 1):

    if i % 5 == 0:
        total_cost -= flour_price

if total_cost > budget:
    print(f'{total_cost - budget:.2f}$ more needed.')

else:
    print(f'Items purchased for {total_cost:.2f}$.')