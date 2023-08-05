
def sum_two_numbers(num1, num2): #  O(1) time complexity
    return num1 + num2

num1 = 23
num2 = 45
result = sum_two_numbers(num1, num2)
print("result ", result)




def is_even(number): # O(1) time complexity
    if(number % 2 == 0):
        return True
    else:
        return False
    
result2 = is_even(45)
print("result2 ", result2)




def get_first_element(lst): # O(1) time complexity
    if len(lst) > 0:
        return lst[0]
    else:
        return None
    
lst = [4,6,8,5]
result3 = get_first_element(lst)
print("result3 ", result3)


def example():
    for x in range(10000):
     print(x)