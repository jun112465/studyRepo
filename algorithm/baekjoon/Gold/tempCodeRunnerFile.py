# https://www.acmicpc.net/problem/7569
# bfs

from collections import deque

M, N, H = map(int, input().split())

tomatoes = []

for h in range(H):
    rows = []
    for n in range(N):
        rows.append(list(map(int, input().split())))
    tomatoes.append(rows)


dirs = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]]
dq = deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 1:
                dq.append((h,n,m,0))
cur_c = 0
while dq:
    h,n,m,c = dq.popleft()
    cur_c = c

    for d in dirs:
        _h = h + d[0]
        _n = n + d[1]
        _m = m + d[2]
        if 0<=_h<H and 0<=_n<N and 0<=_m<M and tomatoes[_h][_n][_m]==0:
            tomatoes[_h][_n][_m] = 1
            dq.append((_h,_n,_m,c+1))


for h in H:
    for n in N:
        for m in M:
            if tomatoes[h][n][m] == 0:
                print(-1)
else:
    print(cur_c)



