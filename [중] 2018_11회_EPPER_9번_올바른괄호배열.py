def solution(open, close, total):
    res = 0
    if close == total:
        return 1
    if open == total:
        res += solution(open, close + 1, total)
    else:
        if open > close:
            res += solution(open, close + 1, total)
            res += solution(open + 1, close, total)
        else:
            res += solution(open + 1, close, total)
    return res


n = int(input())
print(solution(0, 0, n))
