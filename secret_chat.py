message = input()

while True:
    command = input()

    if command =='Reveal':
        break

    if command.startswith('InsertSpace') or command.startswith('Reverse'):
        do, token = command.split(':|:')

        if do == 'InsertSpace':
            message = message[:int(token)] + ' ' + message[int(token):]
            print(message)

        if do == 'Reverse':
            if token in message:
                new_token = token[::-1]
                x = message.index(token)
                message = message[:x]+message[(x+len(token)):] + new_token
                print(message)
            else:
                print('error')

    else:
        do, substring, replacement = command.split(':|:')
        message = message.replace(substring, replacement)
        print(message)

print(f'You have a new text message: {message}')


