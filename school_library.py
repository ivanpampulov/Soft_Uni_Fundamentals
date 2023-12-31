books = input().split('&')

while True:
    command = input()

    if command == 'Done':
        break

    command_list = command.split(' | ')

    if 'Add Book' in command_list and command_list[1] not in books:
        books.insert(0, command_list[1])

    if 'Take Book' in command_list and command_list[1] in books:
        books.remove(command_list[1])

    if 'Swap Books' in command_list and command_list[1] in books and command_list[2] in books:
        index1 = books.index(command_list[1])
        index2 = books.index(command_list[2])
        books[index1], books[index2] = books[index2], books[index1]

    if 'Insert Book' in command_list and command_list[1] not in books:
        books.append(command_list[1])

    if 'Check Book' in command_list and int(command_list[1]) < len(books):
        print(books[int(command_list[1])])

print(', '.join(books))