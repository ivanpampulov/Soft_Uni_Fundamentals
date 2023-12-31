sequence = input("Enter the sequence: ").split()
turns = 0

while sequence:
    current_state = input("Enter a pair of indices to match (or 'end' to quit): ")

    if current_state == 'end':
        print('Sorry, you lose :(')
        break

    indices = current_state.split()

    if len(indices) != 2:
        print('Invalid input! Please provide two indices.')
        continue

    try:
        index1, index2 = map(int, indices)
    except ValueError:
        print('Invalid input! Please enter valid integers.')
        continue

    if index1 < 0 or index1 >= len(sequence) or index2 < 0 or index2 >= len(sequence):
        print('Invalid input! Indices are out of range.')
        continue

    if sequence[index1] == sequence[index2]:
        print(f'Congrats! You have found matching elements - {sequence[index1]}!')
        sequence = [elem for elem in sequence if elem != sequence[index1]]
    else:
        print('Try again!')

    turns += 1

if not sequence:
    print(f'You have won in {turns} turns!')
