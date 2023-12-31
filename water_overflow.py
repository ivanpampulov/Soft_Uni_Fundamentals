capacity = 255
lines = int(input())
total = 0

#logic
for i in range(lines):
    liters = int(input())
    total += liters
    if total > capacity:
        print('Insufficient capacity!')
        total -= liters
        continue

print(total)