def birthday(s, d, m):
    # Write your code here
    return len([1 for i in range(len(s)) if sum(s[i: i+m]) == d])
