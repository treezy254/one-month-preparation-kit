def matchingStrings(strings, queries):
    # Write your code here
    ans = []
    for i in queries:
        ans.append(strings.count(i))
            
    return ans
    
