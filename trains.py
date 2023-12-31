number_of_wagons = int(input())


list_of_wagons = [0] * number_of_wagons


while True:
    command = input()

    if command == 'End':
        break

    tokens = command.split()
    key_word = tokens[0]

    if key_word == 'add':
        people = int(tokens[1])
        list_of_wagons[len(list_of_wagons)-1] += people

    elif key_word == 'insert':
        index1 = int(tokens[1])
        people = int(tokens[2])

        list_of_wagons[index1] += people

    elif key_word == 'leave':
        index1 = int(tokens[1])
        people = int(tokens[2])

        list_of_wagons[index1] -= people

print(list_of_wagons)



