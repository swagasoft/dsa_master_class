
def cubic_space_example(n):
    # O(n^3) time, 
    result = []
    for i in range(n):
        matrix = []
        for j in range(n):
            row = []
            for k in range(n):
                row.append(i * j * k)
            matrix.append(row)
        result.append(matrix)# O(n ^3)
    return result

matrix_size = 2
result_matrix = cubic_space_example(matrix_size)
print(result_matrix)
