N = int(input())
A_list = list(map(int, input().split()))

index_map = {}
index = 0
index_value = {}
for a in A_list:
    index += 1
    index_map[a] = index
    index_value[index] = a
    
flg = False
ans_index = 0
ans_list = []
for key,value in index_map.items():
    ans_index += 1
    j = index_map[ans_index]
    if j == ans_index:
        continue
    ans_list.append(str(ans_index) + " "+ str(j))
    cv = index_value[ans_index]
    cv2 = index_value[j]
    tmpcv = index_map[cv]
    index_map[cv] = index_map[cv2]
    index_map[cv2] = tmpcv    
    index_value[ans_index] = cv2
    index_value[j] = cv
    
    
    flg = True
#    for key,value in index_value.items():
#       print(value)    
#    print("-------")    
if flg == False:
    print(0)
else:
    print(len(ans_list))
    for ans in ans_list:
        print(ans)