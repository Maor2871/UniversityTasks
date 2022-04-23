def winnable(board, show=False, player=0):
    print(board)
    if sum(board) == 0:
        print(True, board)
        return True
    m = len(board)
    for i in range(m):
        for j in range(board[i]):
            munched_board = board[0:i] + [min(board[k], j) for k in range(i, m)]
            if not winnable(munched_board, show, 1-player):
                if show and player == 0:
                    print("recommended move:", board, "-->", munched_board)
                print(True, board)
                return True
    print(False, board)
    return False


winnable([2,1,1], show=True, player=0)
