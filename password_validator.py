import re

password = input()

while True:
    command = input()

    if command == 'Complete':
        break

    if command.startswith('Make Upper'):
        do1, do2, index = command.split()
        index = int(index)

        if len(password) >= index:
            upper_case = password[index]
            password = password[:index] + upper_case.upper() + password[index+1:]
            print(password)
        else:
            pass

    if command.startswith('Make Lower'):
        do1, do2, index = command.split()
        index = int(index)

        if len(password) >= index:
            lower_case = password[index]
            password = password[:index] + lower_case.lower() + password[index + 1:]
            print(password)
        else:
            pass

    if command.startswith('Insert'):
        do, index, char = command.split()
        index = int(index)

        if len(password) >= index:
            password = password[:index] + char + password[index:]
            print(password)

        else:
            pass

    if command.startswith('Replace'):
        do, char, value = command.split()
        value = int(value)

        if char in password:
            char_value = ord(char)
            total = char_value + value
            new_char = chr(total)
            password = password.replace(char, new_char)
            print(password)

        else:
            pass

    elif command.startswith('Validation'):

        if len(password) <= 8:
            print('Password must be at least 8 characters long!')

        pattern = r'\w+$'
        matches = re.findall(pattern, password)
        if len(matches) == 0:
            print('Password must consist only of letters, digits and _!')

        pattern = r'[A-Z]'
        matches = re.findall(pattern, password)
        if len(matches) == 0:
            print('Password must consist at least one uppercase letter!')

        pattern = r'[a-z]'
        matches = re.findall(pattern, password)
        if len(matches) == 0:
            print('Password must consist at least one lowercase letter!')

        pattern = r'[0-9]'
        matches = re.findall(pattern, password)
        if len(matches) == 0:
            print('Password must consist at least one digit!')