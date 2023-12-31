#user input
companions_total = int(input())
adventure = int(input())
total_coins = 0

#logic
for i in range(1, adventure+1):
    if i % 10 == 0:
        companions_total -= 2
    if i % 15 == 0:
        companions_total += 5

    total_coins += 50
    total_coins -= 2 * companions_total

    if i % 3 == 0:
        total_coins -= 3 * companions_total

    if i % 5 == 0:
        total_coins += 20 * companions_total
        if i % 3 == 0:
            total_coins -= 2 * companions_total

print(f"{companions_total} companions received {int(total_coins/companions_total)} coins each.")