key_value_input = input().split()

products = {}

for i in range(0, len(key_value_input), 2):
    key = key_value_input[i]
    value = int(key_value_input[i+1])
    products[key] = value

searched_element = input().split()

for j in searched_element:

    if j in products:
        print(f'We have {products[j]} of {j} left')

    else:
        print(f'Sorry, we don\'t have {j}')