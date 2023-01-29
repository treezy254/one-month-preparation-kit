def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    ans = []
    for i in range(len(arr)):
        max = sum(arr[1:])
        min = sum(arr[:-1])
    ans.append(min)
    ans.append(max)
    print(*ans)
