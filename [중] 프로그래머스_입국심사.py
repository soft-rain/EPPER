def solution(n, times):
    answer = 999999999999
    times.sort()
    start = 1  # 최소 시간 변수
    end = n * times[len(times) - 1]  # 최대 심사 시간 * n명
    temp = 0

    # 이분 탐색
    while start <= end:
        mid = (start + end) // 2
        temp = 0  # mid 시간 동안 심사 가능한 사람의 수

        for i in range(len(times)):
            temp += mid // times[i]  # 총 시간을 심사관들의 심사 시간으로 나눈 각각 i번째 심사관이 심사할 수 있는 사람의 수
        if temp >= n:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1
    return answer


n = int(input())
times = list(map(int, input().split()))
print(solution(n, times))