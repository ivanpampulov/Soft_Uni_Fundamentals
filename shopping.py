#User input

budget = int(input())
total_spend = 0

#logic
while True:
    command = input()

    if command == 'End':
        print('You bought everything needed.')
        break

    money_spend = float(command)
    total_spend += money_spend

    if total_spend > budget:
        print('You went in overdraft!')
        break

