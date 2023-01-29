alpha = list(string.ascii_lowercase)

def pangrams(s):
    # Write your code here
    dope =set([(i) for i in s])
    if len(dope) == len(alpha):
        return "pangram"
    else:
        return "not pangram"
