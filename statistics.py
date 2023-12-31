my_dict = {}
command = input()

while command != 'statistics':

    tokens = command.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])

    if product not in my_dict:
        my_dict[product] = 0

    my_dict[product] += quantity

    command = input()

print('Products in stock:')
for (product, quantity) in my_dict.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {len(my_dict.keys())}')
print(f'Total Quantity: {sum(my_dict.values())}')

