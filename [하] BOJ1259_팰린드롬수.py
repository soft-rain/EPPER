while True:
    N = input()
    if N == "0":
        break
    arr = list(N.strip())
    if N == N[::-1]:
        print("yes")
    else:
        print("no")
