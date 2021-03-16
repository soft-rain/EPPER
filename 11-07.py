# 단순 계산기
# 다시 풀어야 함
n = int(input())
score = [0] * n

for x in range(n):
    score[x] = int(input())

score.sort()
for i in range(1, n + 1):
    if n == 1:
        average = score[i]
    else:
        print(i)
        average = (score[i - 1] + score[i]) / 2
        i = i + 2
        print(i)
        while i != n:
            average = (score[i + 1] + average) / 2
            i = i + 1
print(format(average, ".6f"))
