import re

text = input()
matched_dict = {}
pairs_list = []

pattern = r'(?<=@)[A-Za-z]{3,}@@[A-Za-z]{3,}(?=@)|(?<=#)[A-Za-z]{3,}##[A-Za-z]{3,}(?=#)'
matches = re.findall(pattern, text)

if len(matches) == 0:
    print('No word pairs found!')
    print('No mirror words!')
    quit()

for i in matches:
    if '##' in i:
        pairs = i.split('##')
        first_word = pairs[0]
        second_word = pairs[1]
        if first_word == second_word[::-1]:
            matched_dict[first_word] = second_word

    else:
        pairs = i.split('@@')
        first_word = pairs[0]
        second_word = pairs[1]
        if first_word == second_word[::-1]:
            matched_dict[first_word] = second_word

if len(matched_dict) == 0 and len(matches) > 0:
    print(f'{len(matches)} word pairs found!')
    print('No mirror words!')

else:
    print(f'{len(matches)} word pairs found!')
    print(f'The mirror words are:')
    for key, value in matched_dict.items():
        new_pair = f'{key} <=> {value}'
        pairs_list.append(new_pair)
    print(f'{", ".join(pairs_list)}')







