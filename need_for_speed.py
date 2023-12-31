number_of_cars = int(input())
cars_dict = {}
for i in range(number_of_cars):
    car, kilometers, fuel = input().split('|')
    cars_dict[car] = [int(kilometers), int(fuel)]

while True:
    command = input()

    if command == 'Stop':
        break

    if command.startswith('Drive'):
        do, car, distance, fuel = command.split(' : ')

        if cars_dict[car][1] < int(fuel):
            print('Not enough fuel to make that ride')
        else:
            cars_dict[car][0] += int(distance)
            cars_dict[car][1] -= int(fuel)
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')

        if cars_dict[car][0] >= 100000:
            cars_dict.pop(car)
            print(f'Time to sell the {car}!')

    if command.startswith('Refuel'):
        do, car, fuel = command.split(' : ')
        total_taken = 75 - cars_dict[car][1]
        cars_dict[car][1] += int(fuel)

        if cars_dict[car][1] > 75:
            cars_dict[car][1] = 75
            print(f'{car} refueled with {total_taken} liters')
        else:
            print(f'{car} refueled with {fuel} liters')

    if command.startswith('Revert'):
        do, car, kilometers = command.split(' : ')
        cars_dict[car][0] -= int(kilometers)

        if cars_dict[car][0] < 10000:
            cars_dict[car][0] = 10000

        else:
            print(f'{car} mileage decreased by {kilometers} kilometers')

for key, value in cars_dict.items():
    print(f'{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.')



