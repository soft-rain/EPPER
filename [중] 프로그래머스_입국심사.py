def solution(n, times):
    answer = 9999999999999
    times.sort()
    start = 1
    end = n * times[len(times) - 1]  # 최대 심사 시간 * n명
    temp = 0

    # 이분 탐색
    while start <= end:
        mid = (start + end) // 2
        temp = 0  # mid 시간 동안 심사 가능한 사람의 수

        for i in range(len(times)):
            temp += mid // times[i]
        if temp >= n:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1
    return answer


n = int(input())
times = list(map(int, input().split()))
print(solution(n, times))