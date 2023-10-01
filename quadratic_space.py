
# Example 1
def generate_matrix(n):
    # O(n^2) space, O(n^2) Time
    matrix = []
    for i in range(n):
        row = [] # O(n) space
        for j in range(n):
            row.append(i * j) # O(n^2) space
        matrix.append(row) # O(n^2) space
    return matrix

matrix_size = 3
result_matrix = generate_matrix(matrix_size)
print(result_matrix)





#  Example 3
def generate_all_pairs(items):
    # O(n^2) Space, O(N^2) Time
    pairs = []
    for item1 in items:
        for item2 in items:
            pairs.append((item1, item2))
    return pairs

input_items = [1, 2, 3]
result_pairs = generate_all_pairs(input_items)
print(result_pairs)



