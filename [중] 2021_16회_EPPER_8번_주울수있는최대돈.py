def solution(n, M):
    dp = [0]
    dp.append(M[1])
    print(dp)
    if n > 1:
        dp.append(M[1] + M[2])
    for i in range(3, n + 1):
        dp.append(max(M[i] + dp[i - 2], M[i] + M[i - 1] + dp[i - 3], dp[i - 1]))
    return dp[n]


n = int(input())
M = [0]
M += map(int, input().split())
print(M)
print(solution(n, M))
