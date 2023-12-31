class Party:
    people = []

    def __init__(self):
        pass

command = input()
party1 = Party()

while command != 'End':
    party1.people.append(command)

    command = input()


print(f'Going: {(", ").join(party1.people)}')
print(f'Total: {len(party1.people)}')