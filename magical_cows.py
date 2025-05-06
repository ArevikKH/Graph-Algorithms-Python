MAX_DAYS = 4
C = 8 #maximum number of cows per ferm
M = 1 # visits count

dp = [[0]*(C) for _ in range(MAX_DAYS+1)]

initial_cows = [2,1,1,0,0,0,0,0]

queries = [4]

def solve():
    dp[0] = initial_cows

    for day in range(MAX_DAYS):
        for i in range(1,C+1):
            if i <= C/2:
                dp[day+1][(2*i)-1] += dp[day][i-1]
            else:
               dp[day+1][i-1] += 2 * dp[day][i-1] 
               
    for i in range(M):
        day = queries[i]
        print(SumRow(dp,day))
        
def SumRow(dp,day):
    farms = 0
    for i in range(C):
        farms += dp[day][i]
    return farms

solve()
for row in dp:
    print(row)