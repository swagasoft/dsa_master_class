
def binary_search(arr, target):
    # has O(log n) space 
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
search_index = binary_search(arr, target)

if search_index != -1:
    print(f"Target {target} found at index {search_index}")
else:
    print(f"Target {target} not found!")
