def solution(n, r, goal):
    answer = 0
    n_len = len(n)
    adj = [n_len][n_len]
    time = [n_len]
    total = [n_len]
    inDegree = [n_len]
