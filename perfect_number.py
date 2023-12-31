def is_perfect(some_number: int) -> str:
    divisors_sum = 0

    for divisors in range(1, some_number):
        if some_number % divisors == 0:
            divisors_sum += divisors
    if some_number == divisors_sum:
        return 'We have a perfect number!'
    return "It's not so perfect."

number = int(input())
print(is_perfect(number))