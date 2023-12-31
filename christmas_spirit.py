#Read user input
decoration_qty = int(input())
days_to_Chr = int(input())

ornament_price = 2
skirt_price = 5
garland_price = 3
light_price = 15

ornament_points = 5
skirt_points = 3
garland_points = 10
lights_points = 17


spend = 0
mood = 0
#logic

for i in range(1, days_to_Chr+1):

    if i % 2 == 0:
        spend += ornament_price
        mood += ornament_points

    if i % 3 == 0:
        spend += skirt_price + garland_price
        mood += skirt_points + garland_points + 30

    if i % 5 == 0:
        spend += light_price
        mood += lights_points

    if i % 10 == 0:
        spend += skirt_price + garland_price
        mood -= 20

    if days_to_Chr == 10 and i == 10:
        mood -= 30

    if i % 11 == 0 and i != 1:
        ornament_price *= 3
        skirt_price *= 3
        garland_price *= 3
        light_price *= 3

print(f'Total cost: {spend}')
print(f'Total spirit: {mood}')