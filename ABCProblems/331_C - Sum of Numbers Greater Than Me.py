import bisect
N = int(input())
A_list = list(map(int, input().split()))

sorted_A_List = sorted(A_list)
sum_list = [0]
sum = 0
for a in sorted_A_List:
    sum += a
    sum_list.append(sum)
    
for a in A_list:
    index = bisect.bisect_right(sorted_A_List, a)
    ans = sum_list[len(sum_list) - 1] - sum_list[index]
    
    print(ans)    
    
    