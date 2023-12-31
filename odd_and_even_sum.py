num = input()

def sum_odd_even(number):
    sum_odd = 0
    sum_even = 0
    for i in num:
        i = int(i)
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    return f'Odd sum = {sum_odd}, Even sum = {sum_even}'

print(sum_odd_even(num))

