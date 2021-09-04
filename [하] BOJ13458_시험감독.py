N = int(input())  # 시험장의 개수
arr = list(map(int, input().split()))  # 각 시험장에 있는 응시자 수
B, C = map(int, input().split())  # 총감독관이 감시할 수 있는 응시자 수, 부감독관이 감시할 수 있는 응시자 수
count = 0
for i in arr:
    if i > 0:
        i -= B
        count += 1
    if i > 0:
        count += i // C
        if i % C != 0:
            count += 1

print(count)