while True:

    text = input()

    if text =='end':
        break

    word = text[::-1]

    print(f'{text} = {word}')