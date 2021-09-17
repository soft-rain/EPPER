def solution(s, slen, e, elen):
    answer = 0
    N = slen
    e1 = e2 = -1
    for i in range(0, N):
        for j in range(0, N - 1):
            if e[j] > e[j + 1] or e[j] == e[j + 1] and s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
                e[j], e[j + 1] = e[j + 1], e[j]
    for i in range(0, N):
        if e1 <= s[i]:
            e1 = e[i]
            answer += 1
        elif e2 <= s[i]:
            e2 = e1
            e1 = e[i]
            answer += 1
    return answer


n = int(input())
s = list(map(int, input().split()))
e = list(map(int, input().split()))
slen = len(s)
elen = len(s)
print(solution(s, slen, e, elen))
