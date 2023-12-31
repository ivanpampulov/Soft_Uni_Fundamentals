my_list = list(map(int, input().split(', ')))

positive = [x for x in my_list if x >= 0]
negative = [x for x in my_list if x < 0]
even = [x for x in my_list if x % 2 == 0]
odd = [x for x in my_list if x %2 != 0]

str_positive = ', '.join(map(str, positive))
str_negative = ', '.join(map(str, negative))
str_even = ', '.join(map(str, even))
str_odd = ', '.join(map(str, odd))

print(f'Positive: {str_positive}')
print(f'Negative: {str_negative}')
print(f'Even: {str_even}')
print(f'Odd: {str_odd}')