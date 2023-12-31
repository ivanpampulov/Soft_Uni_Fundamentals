number_balls = int(input())
highes_value = 0
top_weight = 0
top_time = 0
top_quality = 0

#logic
for i in range(number_balls):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality
    if value > highes_value:
        highes_value = value
        top_time = time
        top_weight = weight
        top_quality = quality

print(f"{top_weight} : {top_time} = {int(highes_value)} ({top_quality})")