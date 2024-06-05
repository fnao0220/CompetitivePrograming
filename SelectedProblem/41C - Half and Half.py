A, B, C, X, Y= map(int, input().split())

ans = 9000000000
for i in range(1000000):
   ans  = min(2*C*i + max(X - i,0)*A + max(Y - i,0)*B, ans)



print(ans)
            