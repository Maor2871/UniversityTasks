# 1c_ii
def winnable_mem(board):
    """d = {}
    return winnable_mem_rec(board, count, sucsess)"""
    d = {}
    count = [0]
    success = [0]
    flag = winnable_mem_rec(board, d, count, success)
    print("count:", count, "success:", success)
    return flag

def winnable_mem_rec(board, d, count, success):
    """
        The function receives a board, and a dictionary with already calculated boards, it returns True if the board is winnable, otherwise returns False.
    """

    # Required for dealing with the dictionary.
    board_tupled = tuple(board)

    # This board was already calculated.
    count[0] += 1
    if board_tupled in d:
        success[0] += 1
        return d[board_tupled]
    
    # The previous move cut the last piece, therefore the current player won the game.
    if sum(board)==0:
        d[board_tupled] = True
        return True 

    # Save the length of the board.
    m = len(board)

    # Iterate over the cells of the board.
    for i in range(m):
        for j in range(board[i]):
            
            # Generate the board we would get, if the current player would cut the board in column i, row j.
            munched_board = board[0:i] + [min(board[k], j) for k in range(i,m)]

            # Convert the board to a tuple, so it could be saved as a key in a dictionary.
            munched_board_tupled = tuple(munched_board)
            
            # If the current board was already checked, don't check it again.
            count[0] += 1
            if munched_board_tupled in d:
                success[0] += 1
                # If the current munched board is not winnable, then the current board is.
                if not d[munched_board_tupled]:
                    count[0] += 1
                    success[0] += 1
                    # Save it in the dictionary and return the result.
                    d[board_tupled] = True
                    return True

                # This move won't help to force a win.
                continue
            
            # Check if the current munched board is winnable.
            if not winnable_mem_rec(munched_board, d, count, success):

                # Save the result in the dictionary.
                d[munched_board_tupled] = False

                # And declare that the board is winnable.
                d[board_tupled] = True
                return True             

    # There aren't moves which prevents from the other player to force a win, therefore the current board is not winnable.
    d[board_tupled] = False
    return False


winnable_mem([5]*8)
winnable_mem([5]*16)
