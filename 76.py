N = 101

dp = [[0]*N for _ in range(N)]

dp[1][1] = 1

for i in range(2, N):
    dp[i][i] = 1
    for last in range(1, i):
        diff = i - last
        prev_opts = 0
        for k in range(1, last+1):
            prev_opts += dp[diff][k]
        #print(i, last, prev_opts)
        dp[i][last] += prev_opts

print(sum(dp[100])-1)
