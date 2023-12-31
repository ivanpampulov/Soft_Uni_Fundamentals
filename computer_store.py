total_price = 0
total_with_tax = 0
is_special = True

while is_special:
    parts_price = input()
    if parts_price == 'regular' or parts_price == 'special':
        is_special = False
        if parts_price == 'special':
            total_with_tax = total_with_tax - (total_with_tax * 0.1)
        if total_price == 0:
            print('Invalid order!')
            quit()
        break

    parts_price = float(parts_price)
    if parts_price < 0:
        print('Invalid price!')
        continue

    total_price += parts_price
    total_with_tax += (parts_price * 1.2)

    if total_price == 0:
        print('Invalid order!')


print("Congratulations you've just bought a new computer!")
print(f'Price without taxes: {total_price:.2f}$')
print(f'Taxes: {(total_price *0.2):.2f}$')
print('-----------')
print(f'Total price: {total_with_tax:.2f}$')
