'''
1. 블록을 효율적으로 없애기 위해 세로방향을 리스트로 갖는 새로운 nb를 생성
2. 블록을 없앨 때 for 문으로 remove 하게되면 기존 리스트에 변화가 생기므로 다른 방법을 써야한다.
list compehension으로 리스트를 새로 만들고 없앤 블록만큼 추가("X")하는 방식으로 블록을 없앴다.
'''

def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]

    nb = []
    for j in range(n):
        nb.append([])
        for i in range(m):
            nb[j].append(board[i][j])

    while 1:
        cnt = 0
        check = [[0]*m for _ in range(n)]
        for i in range(n-1):
            for j in range(m-1):
                if nb[i][j] != "X" and nb[i][j] == nb[i+1][j] == nb[i][j+1] == nb[i+1][j+1]:
                    cnt += 1
                    check[i][j] = check[i+1][j] = check[i][j +
                                                           1] = check[i+1][j+1] = 1

        if cnt == 0:
            break

        for i in range(n):
            nb[i] = [nb[i][j] for j in range(m) if check[i][j] != 1]
            answer += m - len(nb[i])
            for j in range(m - len(nb[i])):
                nb[i].insert(0, "X")

    return answer

