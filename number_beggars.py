money = input().split(', ')
beggars = int(input())

int_money = []
for i in money:
    int_money.append(int(i))

final_sums = []
start_index = 0

while start_index < beggars:
    current_beggar = 0
    for index in range(start_index, len(int_money), beggars):
        current_beggar += int_money[index]
    final_sums.append(current_beggar)
    start_index += 1

print(final_sums)