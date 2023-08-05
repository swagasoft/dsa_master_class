
def generate_subsets(elements): # O(4^n)
    n = len(elements)
    subsets = []

    # return all possible combinations
    for i in range(4 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(elements[j])
        subsets.append(subset)

    return subsets


# input_set = [1,2,4,5]
input_set = [1,2,3]
result = generate_subsets(input_set)
print("All subsets:", result)





