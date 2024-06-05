S = str(input())


if S[:3] == "ABC" and  S[3:] != "316" and int(S[3:]) <= 349 and int(S[3:]) >= 0:
    print("Yes")
else:
    print("No")
