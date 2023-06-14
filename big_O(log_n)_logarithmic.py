

def binary_search(arr, target): # O(log n) time complexity
    left = 0
    right = len(arr)
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif  arr[mid] < target:
            left += 1
        else:
            right = mid -1
            
    return -1


arr = [1,3,5,7,8,9,10,11,12]
target = 11

result = binary_search(arr,target)

print("Result ", result)