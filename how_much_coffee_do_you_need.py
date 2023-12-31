is_running = False
total_coffee = 0

while not is_running:
    command = input()

    if command == 'END':
        is_running = True
        break

    if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
        total_coffee += 1

    elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
        total_coffee += 2

if total_coffee > 5:
    print('You need extra sleep')

else:
    print(total_coffee)