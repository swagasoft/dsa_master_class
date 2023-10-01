#example 1
def find_biggest_num(a, b):
    # O(1) space, O(1)time
    biggest = 0
    if a > b:
        biggest = a
        
    if b > a:
        biggest = a

    return biggest

biggest = find_biggest_num(19, 2)
print('biggest_ num -> ',  biggest)




# Example 2
def reverse_array(arr):
    # Reverses sorted  array in place without using additional memory
    # O(1) space, O(n) time
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
my_arr = [1, 2, 3, 4, 5]
reverse_array(my_arr)
print('reversed_arr ',my_arr)



#Example 3
def find_max_in_array(arr):
    # Finds the maximum element in an array using O(1) space
    # O(n)
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

max_element = find_max_in_array([7, 2, 9, 3, 5])
print("Max element:", max_element)


 