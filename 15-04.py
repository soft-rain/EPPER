def solution(numbers):
    ans = []
    sum = 0
    for i in range(9):  ## 다 더해서 합 구하기(numbers[0]~numbers[8])
        sum += numbers[i]
    for i in range(8):  ##0~7 -> numbers[0]~numbers[7]
        for j in range(i + 1, 9):  ##i+1~8 -> numbers[i+1]~numbers[8]
            n1 = numbers[i]
            n2 = numbers[j]
            n = sum - n1 - n2
            if n == 100:
                numbers.remove(n1)
                numbers.remove(n2)
                break
        if n == 100:
            break

    for i in range(7):
        ans.append(numbers[i])
    return ans


numbers = list(map(int, input().split()))  ##리스트로 int 형식으로 ' '로 나눠서 한번에 입력받기
r = solution(numbers)
for i in range(7):  ##0~6
    print(r[i], end=" ")
