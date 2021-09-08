N, r, c = map(int, input().split())


def solution(N, r, c):
    count = 0
    while N > 0:
        size = (2 ** N) // 2
        if N > 1:
            if r < size and c >= size:  ## 2사분면
                count += size ** 2
                c -= size
            elif r >= size and size > c:  ## 3사분면
                count += (size ** 2) * 2
                r -= size
            elif r >= size and size <= c:  ## 4사분면
                count += (size ** 2) * 3
                r -= size
                c -= size
        elif N == 1:
            if r == 0 and c == 1:
                count += 1
            elif r == 1 and c == 0:
                count += 2
            elif r == 1 and c == 1:
                count += 3

        N -= 1
    return count


def solution2(N, r, c):
    count = 0

    while N > 0:
        size = 2 ** (N - 1)
        if N > 1:
            if r >= size and c >= size:  # 4사분면
                count += (size ** 2) * 3
                r -= size
                c -= size
            elif r >= size and c < size:  # 3사분면
                count += (size ** 2) * 2
                r -= size
            elif r < size and c >= size:  # 2사분면
                count += size ** 2
                c -= size
        elif N == 1:
            if r == 0 and c == 1:
                count += 1
            elif r == 1 and c == 0:
                count += 2
            elif r == 1 and c == 1:
                count += 3

        N -= 1
    return count


print(solution2(N, r, c))
