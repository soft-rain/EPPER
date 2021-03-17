def solution(m, n):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = 0  # 거스름돈
    type = 0  # 지불한 화폐 종류
    count = 0  # 지불한 화폐 개수

    change = m - n

    for i in range(8):
        if change >= money[i]:
            type += 1
            count += change // money[i]
            change = change % money[i]

    print(type, end=" ")
    print(count)


m = int(input())
n = int(input())

solution(m, n)
