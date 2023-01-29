def countingSort(arr):
    # Write your code here
    arr.sort()
    new = []
    for i in range(1, arr[-1:]):
        new.append(0)
    return new
