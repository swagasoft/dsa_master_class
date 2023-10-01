def permute(nums):
    #O(n!) space, O(n!) time
    if len(nums) == 0:
        return [[]]
    permutations = []
    for i in range(len(nums)):
        remaining = nums[:i] + nums[i+1:]
        for permutation in permute(remaining):
            permutations.append([nums[i]] + permutation)
    return permutations

print(permute([1,2,3]))