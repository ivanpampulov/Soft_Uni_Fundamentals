#Read user input

orders = int(input())
total = 0

#logic
for i in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_per_day = int(input())

    if price_per_capsule <= 0 or days <= 0 or capsule_per_day <= 0:
        continue

    coffee_price = days * capsule_per_day * price_per_capsule
    total += coffee_price

    print(f'The price for the coffee is: ${coffee_price:.2f}')

print(f'Total: ${total:.2f}')