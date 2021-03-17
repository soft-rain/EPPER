def solution(arr, start, end):
    cnt = 0
    if (start == end) or (start > end):
        return
    if arr[start] == arr[end]:
        solution(arr, start + 1, end - 1)
    else:
        if arr[start] < arr[end]:
            arr[start + 1] = arr[start] + arr[start + 1]
            cnt += 1
            solution(arr, start + 1, end)
        else:
            arr[end - 1] = arr[end] + arr[end - 1]
            cnt += 1
            solution(arr, start, end - 1)
    return cnt


n = int(input())

arr = list(map(int, input().split()))

start = int(0)
end = int(n - 1)

print(solution(arr, start, end))
