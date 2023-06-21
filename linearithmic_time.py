

def linearithmic_time(n):#
    growth = 0
    for i in range(n):
        for j in range(i, n):
            k = 2
            while k < n:
                k = k * 2
            growth += 1
            print("growth rate", growth)
                
                
linearithmic_time(8) 