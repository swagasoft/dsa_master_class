


def generate_permutations(arr):# Big O(N!) Factorial Time complexity
    if len(arr) == 0:
         return [[]] 

    perms_list = [] 

    for i in range(len(arr)):
        remainder = arr[:i] + arr[i+1:]  
        sub_perm_list = generate_permutations(remainder)

        for perm in sub_perm_list:
            perms_list.append([arr[i]] + perm)

    return perms_list

array = [1, 2, 3]
print(generate_permutations(array))














