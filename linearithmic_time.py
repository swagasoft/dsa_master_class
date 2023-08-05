

def linearithmic_time(n):# O(n Log n)
    for i in range(n):#0,1,2,3
        for j in range(i, n):# 0,1,2,3
            k = 2
            while k < n:
                k = k * 2
                
                
linearithmic_time(8) 