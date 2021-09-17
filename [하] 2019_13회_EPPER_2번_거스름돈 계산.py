m = int(input())
n = int(input())
change = m - n
type = 0
count = 0

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in range(8):
    if change >= money[i]:
        type += 1
        count += change // money[i]
        change = change % money[i]
print(type, count)