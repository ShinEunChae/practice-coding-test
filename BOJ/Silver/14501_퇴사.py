N = int(input())
times = []
prices = []

for _ in range(N):
    t, p = map(int, input().split())
    times.append(t)
    prices.append(p)

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + times[i] <= N:
        dp[i] = max(dp[i+1], dp[i + times[i]] + prices[i])
    else:
        dp[i] = dp[i+1]

print(dp[0])
