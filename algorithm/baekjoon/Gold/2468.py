import sys
from collections import deque

N = int(input())
graph = []
max_height = 0
max_cnt = 0

def bfs(a,b,depth):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    q = deque()
    q.append((a,b))
    visited[a][b] = True
    
    while q:
        a,b = q.popleft()
        for x,y in zip(dx,dy):
            ny = y + a
            nx = x + b 
            if 0<=nx<N and 0<=ny<N:
                if not visited[ny][nx] and graph[ny][nx] > depth:
                    visited[ny][nx] = True
                    q.append((ny,nx))

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    max_height = max(max_height, max(graph[i]))

for depth in range(max_height):
    cnt = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > depth:
                cnt += 1
                bfs(i,j,depth)

    max_cnt = max(cnt, max_cnt)

print(max_cnt)
