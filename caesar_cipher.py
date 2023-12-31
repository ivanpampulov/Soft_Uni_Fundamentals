text = input()
new_text = ''
for i in text:
    new_symbol = chr(ord(i) + 3)
    new_text += new_symbol

print(new_text)
