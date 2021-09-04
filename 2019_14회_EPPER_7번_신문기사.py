def solution(r, c, zr, zc, words):
    answer = []
    for i in range(r):
        temp = ""
        for j in range(c):
            for k in range(zc):
                temp += words[i][j]
                # print("temp: ", temp)
                # print("i: ", i)
                # print("j: ", j)
                # print("words: ", words[i][j])
        for m in range(zr):
            answer.append(temp)
    return answer


r, c, zr, zc = input().split()
r = int(r)
c = int(c)
zr = int(zr)
zc = int(zc)

words = []

for i in range(r):
    temp = input()
    if len(temp) > c:
        print("입력 범위를 초과하였습니다.\n")
        exit(1)
    words.append(temp)

answer = solution(r, c, zr, zc, words)

for i in range(r * zr):
    print(answer[i])