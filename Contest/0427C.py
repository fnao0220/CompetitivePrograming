N = int(input())
A_list = list(map(int, input().split()))

beki_map = {}
def pow_k(x, n):
    g = n
    if n == 0:
        beki_map[0] = 1
        return 1
    if n == 1:
        beki_map[1] = 2
        return 2
    if n + 1 not in beki_map:
        K = 1
        while n > 1:
            if n + 1 in beki_map:
                K = beki_map[n + 1]
                continue
            if n % 2 != 0:
                K *= x
            x *= x
            n //= 2
        beki_map[g + 1] = K * x
        return beki_map[g + 1]
    else:
        return beki_map[g + 1]

def dict_search_value(my_dict, search_value):
    r_key = -1
    for key, value in my_dict.items():
        if value == search_value:
            r_key = key
            break
    return r_key

row = []
for n in range(N):
    A_size = pow_k(2,A_list[n])
    row.append(A_size) 
    if len(row) <= 1:
        continue
    while len(row) > 1:
        if row[-2] != row[-1]:
            break
        A_size_pop1 = row.pop()
        A_size_pop2 = row.pop()
#        beki_num = dict_search_value(beki_map, A_size_pop1)
        row.append(A_size_pop1 * 2)

print(len(row))
        