def solution(N, d, p):
    cost = 0  # 총 주유 가격
    min_cost = p[0]  # 처음은 무조건 주유해야 함
    for i in range(N - 1):
        if p[i] < min_cost:  # 지금 도시의 가격이 더 싸면 최소 주유비용 업데이트함
            min_cost = p[i]
        cost += min_cost * d[i]  # 다음 도시까지의 거리 * 주유비용
    return cost


N = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))

print(solution(N, d, p))