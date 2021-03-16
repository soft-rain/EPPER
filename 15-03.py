def solution(n, m):
    answer = 0  # 재고가 떨어지는데 걸리는 날짜
    p = 0  # m일에 한 번 재고가 들어오는 날짜 flag
    while n:  # 재고가 0이 될 때까지 반복
        n -= 1  # 재고 1씩 감소
        answer += 1  # 날짜 1씩 증가
        p += 1
        if p == m:  # m일 지나고 재고 n은 1증가, 날짜 p는 다시 0
            n += 1
            p = 0
    return answer


n, m = map(int, input().split())
answer = solution(n, m)
print(answer)
