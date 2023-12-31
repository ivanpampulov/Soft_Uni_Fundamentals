people = int(input())
capacity = int(input())
courses = 0

#logic
if capacity >= people:
    print('All the persons fit inside the elevator.')
    print('Only one course is needed.')
    quit()
while True:
    courses += 1
    people -= capacity

    if people <= 0:
        break

print(courses)