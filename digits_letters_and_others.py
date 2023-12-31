text = input()

digits = ''
letters = ''
other = ''

for i in text:
    if i.isnumeric():
        digits += i
    elif i.isalpha():
        letters += i

    else:
        other += i

print(digits)
print(letters)
print(other)
