#BFS 큐, FIFO

from collections import deque

def solution(N, adj, M, firstInfected):
    Q = deque([])
    answer = [-1]*(N+1)
    turn=[0]*(N+1)
    
    for t in firstInfected:
        Q.append(t)
        answer[t] = 0
    for i in range(1, N+1):
        turn[i] = len(adj[i]) // 2
    while Q:
        current = Q.popleft()
        for next in adj[current]:
            if next==0:
                break
            turn[next]-=1
            if answer[next]==-1 and turn[next]<=0:
                Q.append(next)
                answer[next]=answer[current]+1
    return answer[1:]

N - int(input())
adj=[][]
for i in range(N):
    for j in range(i):
        adj[i][j] = list(map(int, input().split()))
M=int(input())
firstInfected=[]
firstInfected=list(map(int, input().split()))
