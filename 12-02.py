n = int(input())

num = n % 15
if num == 0:
    num = 15
    # 나머지가 0인 경우는 0번이 아니라 15번

print((n + 14) // 15, end=" ")
print(num)
