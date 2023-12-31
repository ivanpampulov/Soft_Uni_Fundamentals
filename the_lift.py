# Function to distribute tourists on the lift
def distribute_tourists(people, lift):
    for i in range(len(lift)):
        while lift[i] < 4 and people > 0:
            lift[i] += 1
            people -= 1
    return people, lift

# Input
people_waiting = int(input())
current_state = list(map(int, input().split()))

# Distribute tourists and check for various conditions
people_waiting, current_state = distribute_tourists(people_waiting, current_state)

# Check the final state and print the result
if people_waiting == 0 and sum(current_state) < len(current_state) * 4:
    print("The lift has empty spots!")
    print(" ".join(map(str, current_state)))

elif people_waiting > 0 and sum(current_state) == len(current_state) * 4:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join(map(str, current_state)))
else:
    print(" ".join(map(str, current_state)))
