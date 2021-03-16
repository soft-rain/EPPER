def solution(s):
    answer = []
    count = 0
    if s[0] == "1":
        answer += "1"
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            answer.append(chr(65 + count))
            count = 0
        else:
            count += 1

    answer.append(chr(65 + count))

    return "".join(answer)  ##더 좋은 방법..?


s = input()
answer = str(solution(s))
print(answer)
