year = int(input())
is_year_special = False

#logic
while not is_year_special:
    year += 1
    year_as_string = str(year)
    is_year_special = True
    for digit in year_as_string:
        if year_as_string.count(digit) != 1:
            is_year_special = False
            break

print(year)



