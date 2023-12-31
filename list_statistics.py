counter = int(input())
list_positives = []
list_negatives = []

for i in range(counter):
    new_number = int(input())

    if new_number >= 0:
        list_positives.append(new_number)

    else:
        list_negatives.append(new_number)

print(list_positives)
print(list_negatives)
print('Count of positives:', len(list_positives))
print('Sum of negatives:', sum(list_negatives))