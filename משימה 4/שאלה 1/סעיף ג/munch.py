def winnable(board, show=False):
    ''' determines if in a given configuration, represented by board,
        the player who makes the current move can force a win.
        board[i] is the height of column i
        show: if True and the configuration can force win,
        a possible move printed.
    '''
    if sum(board)==0: # halting after the (losing) move (0,0)
        return True 

    m = len(board)
    
    for i in range(m):  # for every column i
        for j in range(board[i]): # for every possible cell (i,j)
            # generate new munched board
            munched_board = board[0:i] + [min(board[k], j) for k in range(i,m)]

            # recursion
            if not winnable(munched_board):  # if munched board is losing
                if show:                
                    print("recommended move:", board, "-->", munched_board) 
                return True             

    return False # current board cannot force win



#examples
##board1 = [5]*4 #rectangular board is winning
##print(winnable(board1, show=True))
##
##board2 = [5,1,1,1,1] #losing board
##print(winnable(board2, show=True))
##
##
##winnable([5,5,5], show=True)
##winnable([5,5,3], show=True)
##winnable([5,5,2], show=True)
##winnable([5,5,1], show=True)
##winnable([5,5,5,5,5],True)
##winnable([6,1,1,1,1,1], show=True)


