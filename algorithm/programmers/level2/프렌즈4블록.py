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
