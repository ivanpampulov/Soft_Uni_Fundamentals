#User input

stars = int(input())
fig = '*'

#logic
for i in range(1, stars+1):
    print(i * fig)
    if i == stars:
        for j in range(stars-1, 0,-1):
            print(j * fig)