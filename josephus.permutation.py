def josephus_permutation(circle, k):
    result = []
    index = 0

    while circle:
        index = (index + k - 1) % len(circle)
        result.append(circle.pop(index))

    return result

# Input
circle = list(map(int, input().split()))
k = int(input())

# Get the Josephus permutation
permutation = josephus_permutation(circle, k)

# Print the result
print("[" + ",".join(map(str, permutation)) + "]")
