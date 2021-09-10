import sys


def solution(N, money):
    for i in range(1, N):
        for j in range(i + 1):
            if j == 0:
                money[i][j] += money[i - 1][0]
            elif j == i:
                money[i][j] += money[i - 1][j - 1]
            else:
                money[i][j] += max(money[i - 1][j - 1], money[i - 1][j])

    return max(money[N - 1])


N = int(input())
money = []
for _ in range(N):
    money.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solution(N, money))
