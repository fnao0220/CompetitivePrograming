S = input()
T = input()

def check(S, t):

    tl = t.lower()
    ans = True
    index = 0    
    for t_char in tl:
        while index < len(S) and t_char != S[index]:
            index += 1
        index += 1                
    return "No" if index > len(S) else "Yes"

print(check(S, T[:2] if T[-1] == "X" else T))
