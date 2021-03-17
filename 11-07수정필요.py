# 단순 계산기
# 다시 풀기
n = int(input())
i = 0
score = []

for i in range(n):
    score.append(int(input()))

score.sort()
i = 0
for i in range(n):
    print(i)
    print(score[i])
    if n == 1:
        avg = score[i]
    else:
        avg = (score[i] + score[i + 1]) / 2
        i += 2
        while i != n:
            avg = (score[i] + avg) / 2
            i += 1

print(format(avg, "%.6f"))
