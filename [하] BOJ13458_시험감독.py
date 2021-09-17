N = int(input())  # 시험장의 개수
A = list(map(int, input().split()))  # 각 시험장에 있는 응시자 수
B, C = map(int, input().split())  # 총감독관이 감시할 수 있는 응시자 수, 부감독관이 감시할 수 있는 응시자 수


def solution(N, A, B, C):
    ans = 0
    for i in range(N):
        A[i] -= B  # 모든 시험장에서 총 감독관이 감시할 수 있는 응시자 수 빼기
        ans += 1  # 총감독관 수 더함

        if A[i] > 0:
            ans += A[i] // C
            if A[i] % C != 0:
                ans += 1
            else:
                ans += 0

    return ans


print(solution(N, A, B, C))