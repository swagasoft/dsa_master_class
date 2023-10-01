
def power_set(nums):
    #O(2^n) timer, O(2^n) space
    result = [[]]
    for num in nums:
        result += [subset + [num] for subset in result]
    return result

print(power_set([4,6,2]))