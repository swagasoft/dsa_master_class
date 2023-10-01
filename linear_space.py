def generate_array(n):
    #  Dynamic Array with O(n) Space Complexity:
    # O(n) Time
    dynamic_array = []
    for i in range(n):
        dynamic_array.append(i) # O(n)
    return dynamic_array

result = generate_array(10)
print(result)





# example 2
def process_input(input_data):
    # Storing Input Data with O(n) Space Complexit
    storage = []
    for item in input_data:
        storage.append(item)
    return storage

# result = process_input([10, 20, 30, 40, 50])
# print('storage' ,result)




#example 3
def linear_recursive(n):
    # Linear Recursive Function with O(n) Space Complexity
    if n <= 0:
        return
    linear_recursive(n - 1)
    print(n)

# linear_recursive(5)


