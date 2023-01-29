def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    d1 = 0
    d2 = 0
    
    for i in range(0, n):
        for j in range(0, n):
            
            if i == j:
                d1 += arr[i][j]
            
            if n - j - 1 == i:
                d2 += arr[i][j]
                
    return abs(d1 - d2)
 
