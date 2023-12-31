shopping_list = input().split('!')

while True:
    command = input()

    if command == 'Go Shopping!':
        break

    command_list = command.split()

    if 'Urgent' in command_list and command_list[1] not in shopping_list:
            shopping_list.insert(0, command_list[1])

    if 'Unnecessary' in command_list and command_list[1] in shopping_list:
        shopping_list.remove(command_list[1])

    if 'Correct' in command_list and command_list[1] in shopping_list:
            index1 = shopping_list.index(command_list[1])
            shopping_list.insert(index1, command_list[2])
            shopping_list.pop(index1 + 1)

    if 'Rearrange' in command_list and command_list[1] in shopping_list:
            shopping_list.remove(command_list[1])
            shopping_list.append(command_list[1])

print(', '.join(shopping_list))
