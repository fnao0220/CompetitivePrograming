from itertools import product
N, M = map(int, input().split())

relations = set()

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    relations.add((a, b))

ans = -1
for pro in product((0, 1), repeat=N):
    member_list = []
    for i in range(len(pro)):
        if pro[i] == 0:
            continue
        member_list.append(i)
    
    if ans  > sum(pro):
        continue
    
    max_faction = 0
    faction_menber = 0
    for i in range(len(member_list)):
        add_flg = True
        for j in range(i + 1, len(member_list)):
            member_i = member_list[i]
            member_j = member_list[j]
            
            if member_i == member_j:
                continue
            if (member_i, member_j) not in  relations:
                add_flg = False
                break
        if add_flg:
            faction_menber += 1
    ans = max(ans, faction_menber)    
    
print(ans)

def print_varsize():
    import types
    print("{}{: >15}{}{: >10}{}".format('|','Variable Name','|','  Size','|'))
    print(" -------------------------- ")
    for k, v in globals().items():
        if hasattr(v, 'size') and not k.startswith('_') and not isinstance(v,types.ModuleType):
            print("{}{: >15}{}{: >10}{}".format('|',k,'|',str(v.size),'|'))
        elif hasattr(v, '__len__') and not k.startswith('_') and not isinstance(v,types.ModuleType):
            print("{}{: >15}{}{: >10}{}".format('|',k,'|',str(len(v)),'|'))
print_varsize()