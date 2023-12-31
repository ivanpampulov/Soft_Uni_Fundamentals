sequence = input().split()
is_command = True
found_numbers = []
int_current_state = []
turns = 0

while is_command:
    current_state = input()
    turns += 1
    found_numbers = []
    int_current_state = []

    if current_state == 'end' and len(sequence) != 0:
        is_command = False
        print('Sorry you lose :(')
        for char in sequence:
            print(char, end=' ')
        continue

    for integer in current_state.split():
        integer = int(integer)
        int_current_state.append(integer)

    if int_current_state[0] == int_current_state[1] or int_current_state[0] < 0 or int_current_state[1] < 0:
        print('Invalid input! Adding additional elements to the board')
        middle = len(sequence) // 2
        sequence = sequence[0:middle] + [f'-{turns}a'] + [f'-{turns}a'] + sequence[middle:]
        continue

    for index in int_current_state:
        found_numbers.append(sequence[index])
    if found_numbers[0] == found_numbers[1]:
        print(f'Congrats! You have found matching elements - {found_numbers[0]}!')

        for k in found_numbers[:]:
            sequence.remove(k)

    if found_numbers[0] != found_numbers[1]:
        print('Try again!')

    if len(sequence) == 0:
        print(f'You have won in {turns} turns!')
        quit()










