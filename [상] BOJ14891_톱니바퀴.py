import sys
from collections import deque


def play(num, dir):
    pre_pole = wheel[num][6]
    tmp_dir = dir
    for i in range(num - 1, -1, -1):
        tmp_dir *= -1
        if wheel[i][2] == pre_pole:
            break
        pre_pole = wheel[i][6]
        wheel[i].rotate(tmp_dir)
    pre_pole = wheel[num][2]
    tmp_dir = dir
    for i in range(num + 1, 4, 1):
        tmp_dir *= -1
        if wheel[i][6] == pre_pole:
            break
        pre_pole = wheel[i][2]
        wheel[i].rotate(tmp_dir)

    wheel[num].rotate(dir)


wheel = []

for _ in range(4):
    wheel.append(deque(list(input())))

K = int(sys.stdin.readline())
for i in range(K):
    num, dir = map(int, sys.stdin.readline().split())
    play(num - 1, dir)
plus = 1
total = 0
for i in range(4):
    if wheel[i][0] == "1":
        total += plus
    plus *= 2
print(total)
