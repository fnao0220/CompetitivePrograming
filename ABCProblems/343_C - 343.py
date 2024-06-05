N = int(input())


def is_palindrome(S):
    return S == S[::-1]

n = 0
tmp_ans = 0
ans = 0
while N >= tmp_ans:
    n += 1
    tmp_ans = n ** 3
    if tmp_ans > N:
        break
    if is_palindrome(str(tmp_ans)):
        ans = tmp_ans

print(ans)
    