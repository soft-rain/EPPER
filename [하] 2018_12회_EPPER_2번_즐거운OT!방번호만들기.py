n = int(input())
num = n % 15
if num == 0:
    num = 15
print((n + 14) // 15, num)
