import re

count_barcodes = int(input())
pattern = r'^@[#]+[A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1}@[#]+'

total = ''

for i in range(count_barcodes):
    barcode = input()
    matches = re.findall(pattern, barcode)

    if not matches:
        print('Invalid barcode')

    else:
        value = ''.join(matches)
        for j in value:
            if j.isnumeric():
                total += j

        if total == '':
            print('Product group: 00')

        else:
            print(f'Product group: {total}')
            total = ''





