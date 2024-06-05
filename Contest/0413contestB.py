S = input()

cntmap = {}

for s in S:
    cnt = 0
    if s in cntmap:
        cnt = cntmap[s]
    cnt += 1
    cntmap[s] = cnt

cnt_type_map = {}
for s, cnt in cntmap.items():
    cnt_type = 0
    if cnt in cnt_type_map:
        cnt_type = cnt_type_map[cnt]
    cnt_type += 1
    cnt_type_map[cnt] = cnt_type 

ans = "Yes"
for i in range(101):
    if i not in cnt_type_map:
        continue
    if cnt_type_map[i] >= 3 or cnt_type_map[i] == 1:
        ans = "No"
        break
    
print(ans)