#User input

budget = float(input())
flour_price = float(input())
egg_price = flour_price * 0.75
milk_price = (flour_price + (flour_price * 0.25))/4
breads_total = 0
colored_eggs = 0
current_bread_count = 0

#logic
total_spend = 0

while budget > total_spend:
    cost_bread = flour_price + egg_price + milk_price
    money_left = budget - total_spend

    if cost_bread > money_left:
        break

    total_spend += cost_bread
    breads_total += 1
    colored_eggs += 3
    current_bread_count += 1



    if current_bread_count == 3:
        substracted_eggs = breads_total - 2
        colored_eggs -= substracted_eggs
        current_bread_count = 0

print(f'You made {breads_total} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')