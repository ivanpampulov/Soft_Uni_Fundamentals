number_of_pieces = int(input())
my_dict = {}

for i in range(number_of_pieces):
    piece, composer, key = input().split('|')
    my_dict[piece] = [composer, key]

while True:
    input_command = input()

    if input_command == 'Stop':
        break

    if input_command.startswith('Add'):
        command, piece, composer, key = input_command.split('|')
        if piece not in my_dict:
            my_dict[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            key = [key for key in my_dict.keys() if key == command[1]]
            print(f'{"".join(key)} is already in the collection!')

    elif command[0] == 'Remove':
        if command[1] in my_dict:
            my_dict.pop(command[1])
            print(f'Successfully removed {command[1]}!')
        else:
            print(f'Invalid operation! {command[1]} does not exist in the collection.')

    elif command[0] == 'ChangeKey':
        if command[1] in my_dict:
            working_list = my_dict[command[1]]
            working_list[1] = command[2]
            my_dict[command[1]] = working_list
            print(f'Changed the key of {command[1]} to {command[2]}!')

        else:
            print(f'Invalid operation! {command[1]} does not exist in the collection.')

for key, value in my_dict.items():
    print(f'{key} -> Composer: {"".join(value[0])}, Key: {"".join(value[1])}')