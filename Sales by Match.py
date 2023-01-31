def sockMerchant(n, ar):
    # Write your code here
    mine = set(ar)
    counter = {}
    ans = 0
    for i in ar:
        if i not in counter:
            counter[i] = 0
        counter[i] += 1
        
    for i in mine:
        ans += counter[i] // 2
        
    return ans
