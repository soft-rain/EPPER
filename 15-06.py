def solution(m, a):
    stack = []
    alist = a.split()
    for i in alist:
        if i == "+":
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 + op2)
        elif i == "-":
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 - op2)
        elif i == "*":
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 * op2)
        elif i == "/":
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 / op2)
        else:
            stack.append(int(i))
    return int(stack.pop())


m = int(input())
a = input()
answer = solution(m, a)
print(answer)