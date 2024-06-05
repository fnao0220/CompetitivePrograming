from itertools import product

S = input()
T = input()

air_cord = ""
ans = "No"
for pro in product((0, 1), repeat=len(T)):
    air_cord = ""
    if sum(pro) == 3:
        t = T.lower()
        match = True
        for tn in t:
            if -1 == S.find(tn):
                match = False
                break
        if match == True:
            ans = "Yes"
            break
    elif sum(pro) == 2:
        t = T.lower()
        for tn in t:
            if -1 != S.find(tn):
                air_cord += tn
        air_cord += "X"
        if air_cord == T:
            ans = "Yes"
            break
print(ans)