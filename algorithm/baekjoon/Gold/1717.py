from ctypes import Union
import sys

'''
union-find 최적화 방식

1. 랭크를 이용한 Union
더 낮은 랭크의 집합을 높은 랭크의 집합에 합친다. (높이 변화 x)
2. 경로 압축
합치는 집합 중 하나의 집합의 모든 노드들의 parent 값을 바꿔주는 것
'''


def getParent(el):
    if el == setList[el][0]:
        return setList[el]
    return getParent(setList[el][0])

n, m = map(int, sys.stdin.readline().split())
setList = [[i,0] for i in range(n+1)]


for _ in range(m):
    cmd, x, y = map(int, sys.stdin.readline().split())

    if cmd == 0:
        px = getParent(x)
        py = getParent(y)
        
        if px[1] < py[1]:
            setList[px[0]][0] = py[0]
        elif px[1] > py[1]:
            setList[py[0]][0] = px[0]
        else:
            setList[px[0]][0] = py[0]
            setList[py[0]][1] += 1
    
    if cmd == 1:
        px = getParent(x)
        py = getParent(y)
        if px[0] == py[0]:
            print("YES")
        else:
            print("NO")

# print(setList)




