def solution(n, arr):
    arr.sort()
    i = 0
    if n == 1:
        avg = arr[i]
    else:
        avg = (arr[i] + arr[i + 1]) / 2

        i += 2
        while i != n:
            avg = (arr[i] + avg) / 2

            i += 1
    return avg


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print("{:.6f}".format(solution(n, arr)))