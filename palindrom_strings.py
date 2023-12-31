

def found_palindroms():
    my_list = input().split()
    palindrom = input()

    new_list = [word for word in my_list if word == word[::-1]]
    found = len([x for x in my_list if x == palindrom])
    print(new_list)
    print(f'Found palindrome {found} times')



found_palindroms()

