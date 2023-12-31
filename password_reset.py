text = input()
new_password = ''
substring = ''

while True:
    command = input()

    if command == 'Done':
        break

    if command == 'TakeOdd':
        for i in range(1, len(text)+1):
            if i % 2 == 0:
                new_password += text[i-1]
        text = new_password
        print(text)

    elif command.startswith('Cut'):
        do, index, length = command.split()
        text = text[:int(index)] + text[int(index) + int(length):]
        print(text)

    elif command.startswith('Substitute'):
        do, substr1, substr2 = command.split()
        if substr1 in text:
            text = text.replace(substr1, substr2)
            print(text)
        else:
            print('Nothing to replace!')

print(f'Your password is: {text}')
