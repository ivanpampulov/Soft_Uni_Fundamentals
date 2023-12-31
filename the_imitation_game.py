text = input()
new_text = ''
while True:
    command = input()

    if command == "Decode":
        break

    decoding = command.split('|')

    if decoding[0] == 'Move':
        text = text[int(decoding[1]):] + text[:int(decoding[1])]

    elif decoding[0] == 'Insert':   

        if len(text) < int(decoding[1])+1:
            text += decoding[2]
        else:
            for i in range(len(text)):
                if i == (int(decoding[1])):
                    new_text += decoding[2]
                new_text += text[i]
            text = new_text
            new_text = ''

    elif decoding[0] == 'ChangeAll':
        text = text.replace(decoding[1], decoding[2])

print(f'The decrypted message is: {text}')