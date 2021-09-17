answer = 0


def solution(arr, start, end):
    global answer
    if start == end or start > end:
        return answer
    if arr[start] == arr[end]:
        return solution(arr, start + 1, end - 1)
    else:
        if arr[start] < arr[end]:
            arr[start + 1] = arr[start + 1] + arr[start]
            answer += 1
            return solution(arr, start + 1, end)
        else:
            arr[end - 1] = arr[end] + arr[end - 1]
            answer += 1
            return solution(arr, start, end - 1)
    return answer


n = int(input())
arr = list(map(int, input().split()))
start = 0
end = n - 1
print(solution(arr, start, end))