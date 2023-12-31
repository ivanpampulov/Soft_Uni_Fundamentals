#Read user input

n = int(input())
char1 = ','
char2 = '.'
char3 = '_'


#logic
for i in range(n):
    string = input()
    if char1 in string:
        print(f'{string} is not pure!')
    elif char2 in string:
        print(f'{string} is not pure!')
    elif char3 in string:
        print(f'{string} is not pure!')

    else:
        print(f'{string} is pure.')
