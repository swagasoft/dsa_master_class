
def counter_num(lst):# O^2 time complexity
    lenn = len(lst)
    
    for i in range(lenn):
        for j in range(lenn):
            print("result ", i, j)
            
            
arr = [1,2,3,4,5]
counter_num(arr)