numbers = input().split()

while True:
    command = input()

    if command == 'Finish':
        break

    command_list = command.split()

    if 'Add' in command_list:
        numbers.append(command_list[1])

    if 'Remove' in command_list and command_list[1] in numbers:
        numbers.remove(command_list[1])

    if 'Replace' in command_list and command_list[1] in numbers:
        index1 = numbers.index(command_list[1])
        numbers.insert(index1, command_list[2])
        numbers.pop(index1 + 1)

    if 'Collapse' in command_list:
        numbers = list(map(int, numbers))
        numbers = [x for x in numbers if x >= int(command_list[1])]
        numbers = list(map(str, numbers))

print(' '.join(numbers))