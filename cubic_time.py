
def cubic_time(arr):  #N * N * N = O(N^3).
    n = len(arr)
    growth = 0
    
    for i in range(n): #N
        for j in range(n):#N
            for k in range(n):#N
                growth += 1
    print("Growth ", growth)
    
    
# arr = [3,6,8,2,1,2,3,3]
# arr = [3,6,8,2]
arr = [3,6]
cubic_time(arr)


