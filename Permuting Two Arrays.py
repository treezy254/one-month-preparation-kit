def twoArrays(k, A, B):
    # Write your code here
    A.sort(reverse=True)
    B.sort()
    dope = []
    for i in range(len(A)):
        dope.append(A[i] + B[i])
    dope.sort()
    if dope[0] < k:
        return 'NO'
    else:
        return 'YES'
