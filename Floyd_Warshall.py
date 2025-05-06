n = 4
m =[
    [0, 4, 1, 100],
    [100, 0, 6, 100],
    [4, 1, 0, 2],
    [100, 100, 100, 0]
]

def floydWarshall(m):
    dp = m
    next_ = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if m[i][j] != 100:
                next_[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    next_[i][j] = next_[i][k]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = -100
                    next_[i][j] = -1

    return dp

print(floydWarshall(m))