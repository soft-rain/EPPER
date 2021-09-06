def solution(s):
    arr = []
    count = 0

    if s[0] == "1":
        arr += "1"

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            arr += chr(65 + count)
            count = 0
        else:
            count += 1
    arr += chr(65 + count)

    return "".join(arr)


s = list(input())
print(solution(s))