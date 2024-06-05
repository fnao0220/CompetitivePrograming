def estimate_development_time(N, X, F, S):
    """
    N: ソースコードの行数
    X: 1 時間あたりのコード行数
    F: 開発を続ける場合の減少行数
    S: 睡眠をとる場合の増加行数
    """
    lines_written = 0
    hours = 0
    can_write = X
    ans = 0
    remain_lines = N
    while lines_written < N:

        
        if can_write <= X and can_write != 0 and remain_lines != X:
            #開発継続        
            lines_written += can_write
            # 開発を行って今後かける量
            can_write =  max(0,X - F)
            remain_lines = N - lines_written
            ans += 1
        else:
            # 睡眠を行って今後書ける量
            can_write =  min(X,X + S)
            ans += 3
                    


    return ans

# 入力例1
N = 80
X = 30
F = 10
S = 30

estimated_hours = estimate_development_time(N, X, F, S)
print(f"最短で {estimated_hours} 時間でソースコードを書き終えることができます。")