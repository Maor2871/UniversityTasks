# Skeleton file for HW4 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.


# Change the name of the file to include your ID number (hw4_ID.py).
import math

# For MyTest, not used in the implementation.
from itertools import product
from random import choice, randint
from copy import deepcopy


##############
# Question 1 #
##############


# 1b
def change_v2(amount, coins, tail=[]):
    """
        The Recursion receives an amount and available coins. It returns a list with all the coins combinations which their sums equals the amount.
        tail accumulates all the coins that were accumulated before the call to the function.
        Note that the time complexity of the change problem is exponential (terrible), therefore slicing and concatenating is relativly ok here.
    """

    # Greate, the combination in the tail is precise, no need for more coins.
    if amount == 0:
        if tail:
            return [tail]
        return []

    # No coins left and amount was not reached.
    if coins == []:
        return []

    # Check all the combinations with the first coin. (If its greater than the requried amount, don't bother).
    combinations_with_first = []

    # Check if the first coin does not exceed the required amount by itself.
    if coins[0] <= amount:

        # Find all the combinations with the first coin used (we wish to send a new copy of tail, the concatenation does it by definition).
        combinations_with_first = change_v2(amount - coins[0], coins, tail=tail+[coins[0]])

    # Check all the combinations without the first coin. Return all the combinations accumulated after all.
    return combinations_with_first + change_v2(amount, coins[1:], tail=tail)


# 1c_ii
def winnable_mem(board):
    d = {}
    return winnable_mem_rec(board, d)

def winnable_mem_rec(board, d):
    """
        The function receives a board, and a dictionary with already calculated boards, it returns True if the board is winnable, otherwise returns False.
    """

    # Required for dealing with the dictionary.
    board_tupled = tuple(board)

    # This board was already calculated.
    if board_tupled in d:
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
            if munched_board_tupled in d:

                # If the current munched board is not winnable, then the current board is.
                if not d[munched_board_tupled]:

                    # Save it in the dictionary and return the result.
                    d[board_tupled] = True
                    return True

                # This move won't help to force a win.
                continue
            
            # Check if the current munched board is winnable.
            if not winnable_mem_rec(munched_board, d):

                # Save the result in the dictionary.
                d[munched_board_tupled] = False

                # And declare that the board is winnable.
                d[board_tupled] = True
                return True             

    # There aren't moves which prevents from the other player to force a win, therefore the current board is not winnable.
    d[board_tupled] = False
    return False


##############
# Question 2 #
##############


# 2a
def legal_path(A, vertices):
    """
        The function receives a matrix of a graph, A, and a list of vertices. It returns True if the vertices in the list by their order, are a path in the graph.
        Note that A cannot be empty.
    """

    # Iterate over the list of vertices.
    for i in range(len(vertices) - 1):

        # If the current bow is not on the graph, this is not a legal path.
        if not A[vertices[i]][vertices[i+1]]:
            return False

    # All the bows in the vertices list are on the graph, this is a legal path.
    return True


# 2c
def path_v2(A, s, t, k):
    if k == 0:
        return s == t

    if k == 1:
        if A[s][t] == 1:
            return True
        return False

    for i in range(len(A)):
        mid = k // 2
        if path_v2(A, s, i, mid) and path_v2(A, i, t, k - mid):
            return True
    return False


# 2d
def path_v3(A, s, t):
    if s == t:
        return True

    for i in range(len(A)):
        if A[s][i] == 1:
            A[s][i] = 0
            if path_v3(A, i, t):
                return True
    return False


path_v3_a = None
path_v3_b = ([[0, 1, 0], [1, 0 ,1], [0, 0, 0]], 0, 2)
path_v3_c = ([[0, 1, 0], [0, 0 ,1], [0, 0, 0]], 0, 0)
path_v3_d = ([[0, 1, 0], [1, 0 ,0], [0, 0, 0]], 0, 2)


##############
# Question 3 #
##############


# 3a
def can_create_once(s, L):
    """
        The function receives a list and a number s. It returns True if we can add or subtract the numbers in the list, when each number is used exactly once, and reach s.
    """

    # Time to check.
    if not L:

        # The current sum made it, congrates.
        if s == 0:
            return True

        # Not this time.
        return False

    # Save the value of the last element in the list and remove it from the list.
    last_element = L.pop()

    # Check if there's a combination with the last elemnt as positive, or with the last element as negative.   
    if can_create_once(s - last_element, L) or can_create_once(s + last_element, L):
        return True

    # Recover the list (necessary for the second call of the parent).
    L.append(last_element)
    
    return False

# 3b
def can_create_twice(s, L):
    """
        The function receives a list and a number s. It returns True if we can add or subtract the numbers in the list, when each number is used not more than twice, and reach s.
    """

    # The current sum made it, congrates.
    if s == 0:
        return True

    # No more options, dead end.
    if not L:
        return False

    # Save the value of the last element in the list and remove it from the list.
    last_element = L.pop()
    
    # Check if there's a combination with the first elemnt as positive, or negative, or twice positive, or twice negative, or without the first element at all.
    if can_create_twice(s - last_element, L) or can_create_twice(s + last_element, L) or can_create_twice(s + 2 * last_element, L) or can_create_twice(s - 2 * last_element, L) or can_create_twice(s, L):
        return True

    # Recover the list (necessary for the following calls of the parent).
    L.append(last_element)

    return False

# 3c
def valid_braces_placement(s, L):
    """
        The function receives a list of numbers and operations. It returns True if there exists a braces placement on the expression which produces the results s.
    """

    # Check if the current braces placement is valid.
    if len(L) == 1:
        if L[0] == s:
            return True
        return False
    
    # Iterate over the list.
    for i in range(0, len(L) - 1, 2):
        
        # Place the braces in i.
        braces_in_i = L[:i] + [eval(str(L[i]) + L[i + 1] + str(L[i + 2]))] + L[i+3:]

        # Try to add more braces, check if can reach s.
        if valid_braces_placement(s, braces_in_i):
            return True

    # No braces placement did the job.
    return False


##############
# Question 4 #
##############


# 4a
def grid_escape1(B):
    """
        The function recieves a grid and returns True if it's possible to escape.
        Note that it is possible to move right or up only.
    """

    return grid_escape_from_1(B, (0, 0))

def grid_escape_from_1(B, initial_location):
    """
        The function receives a grid and initial location (tuple- (row, col)) and returns True if it is possible to escape the grid from the received location.
        Note that it is possible to move right or up only.
    """

    # Horray, we reached n-1, n-1.
    if initial_location == (len(B) - 1, len(B) - 1):
        return True

    # Unpack the initila location.
    current_row, current_col = initial_location

    # Save the current step.
    step = B[current_row][current_col]
    
    # Check if we can go up and stay in bound.
    if current_row + step < len(B):
       
        # Move up and check if we can escape from this route.
        if grid_escape_from_1(B, (current_row + step, current_col)):
            return True

    # Check if we can go right and stay in bound.
    if current_col + step < len(B[0]):
       
        # Move right! check if we can escape from this route.
        if grid_escape_from_1(B, (current_row, current_col + step)):
            return True

    # There's no escape route.
    return False

# 4b
def grid_escape2(B):
    """
        The function recieves a grid and returns True if it's possible to escape.
        Note that it is possible to move right, left, up or down.
    """

    return grid_escape_from_2(B, (0, 0), [])

def grid_escape_from_2(B, initial_location, already_checked=[]):
    """
        The function receives a grid and initial location (tuple- (row, col)) and returns True if it is possible to escape the grid from the received location.
        Note that it is possible to move right, left, up or down.
        Already checked is a list of locations that were already checked. We don't want cycles.
    """

    already_checked.append(initial_location)
    
    # Horray, we reached n-1, n-1.
    if initial_location == (len(B) - 1, len(B) - 1):
        return True

    # Unpack the initila location.
    current_row, current_col = initial_location

    # Save the current step.
    step = B[current_row][current_col]
    
    # Check if we can go up and stay in bound.
    if current_row + step < len(B) and (current_row + step, current_col) not in already_checked:
       
        # Move up and check if we can escape from this route.
        if grid_escape_from_2(B, (current_row + step, current_col), already_checked):
            return True

    # Check if we can go down and stay in bound.
    if current_row - step >= 0 and (current_row - step, current_col) not in already_checked:
       
        # Move up and check if we can escape from this route.
        if grid_escape_from_2(B, (current_row - step, current_col), already_checked):
            return True

    # Check if we can go right and stay in bound.
    if current_col + step < len(B[0]) and (current_row, current_col + step) not in already_checked:
       
        # Move right and check if we can escape from this route.
        if grid_escape_from_2(B, (current_row, current_col + step), already_checked):
            return True

    # Check if we can go left and stay in bound.
    if current_col - step >= 0 and (current_row, current_col - step) not in already_checked:

        # Move left and check if we can escape from this route.
        if grid_escape_from_2(B, (current_row, current_col - step), already_checked):
            return True

    # There's no escape route.
    return False


##########
# Tester #
##########


def test():
    # 1b
    if len(change_v2(5, [1, 2, 3])) != 5:
        print("error in change_v2")

    # 1c
    if winnable_mem([5, 5, 3]) or not winnable_mem([5, 5, 5]):
        print("error in winnable_mem")

    # 2a
    A = [[0, 1, 1, 0, 0], [1, 0, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    if not legal_path(A.copy(), [0, 1, 2, 3]) or \
            not legal_path(A.copy(), [0, 1, 2, 3, 0, 1]) or \
            legal_path(A.copy(), [1, 2, 3, 4]):
        print("error in legal_path")

    # 2d
    if path_v3_a != None and not path_v3(path_v3_a[0], path_v3_a[1], path_v3_a[2]):
        print("error in path_v3 or with path_v3_a")

    if path_v3_b != None and not path_v3(path_v3_b[0], path_v3_b[1], path_v3_b[2]):
        print("error in path_v3 or with path_v3_b")

    if path_v3_c != None and path_v3(path_v3_c[0], path_v3_c[1], path_v3_c[2]):
        print("error in path_v3 or with path_v3_c")

    if path_v3_d != None and path_v3(path_v3_d[0], path_v3_d[1], path_v3_d[2]):
        print("error in path_v3 or with path_v3_d")

    # 3a
    if not can_create_once(6, [5, 2, 3]) or not can_create_once(-10, [5, 2, 3]) \
            or can_create_once(9, [5, 2, 3]) or can_create_once(7, [5, 2, 3]):
        print("error in can_create_once")
    # 3b
    if not can_create_twice(6, [5, 2, 3]) or not can_create_twice(9, [5, 2, 3]) \
        or not can_create_twice(7, [5, 2, 3]) or can_create_once(19, [5, 2, 3]):
        print("error in can_create_twice")
    # 3c
    L = [6, '-', 4, '*', 2, '+', 3]
    if not valid_braces_placement(10, L.copy()) or \
            not valid_braces_placement(1, L.copy()) or \
            valid_braces_placement(5, L.copy()):
        print("error in valid_braces_placement")

    B1 = [[1, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 1, 2]]
    B2 = [[2, 3, 1, 2], [2, 2, 2, 2], [2, 2, 3, 2], [2, 2, 2, 2]]
    B3 = [[2, 1, 2, 1], [1, 2, 1, 1], [2, 2, 2, 2], [4, 4, 4, 4]]

    # 4a
    if not grid_escape1(B1.copy()):
        print("error in grid_escape1 - B1")
    if grid_escape1(B2.copy()):
        print("error in grid_escape1 - B2")
    if grid_escape1(B3.copy()):
        print("error in grid_escape1 - B3")

    # 4b
    if not grid_escape2(B1.copy()):
        print("error in grid_escape2 - B1")
    if not grid_escape2(B2.copy()):
        print("error in grid_escape2 - B2")
    if grid_escape2(B3.copy()):
        print("error in grid_escape2 - B3")


class MyTest:
    """
        Tester.
    """

    def test(self):
        """
            Run the tester.
        """
    
        # Q 1

        # b
        self.change_v2_check_results(results=change_v2(amount=5, coins=[1, 2, 3], tail=[]),
                                expected=[[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 3], [1, 2, 2], [2, 3]])
        self.change_v2_check_results(results=change_v2(amount=0, coins=[]), expected=[])

        # c
        for board_size in range(5):
            for board in product(range(1, board_size + 1), repeat=board_size):
                board = list(board)
                if self.winnable(board) is not winnable_mem(board):
                    print("error in winnable_mem, board:", board)
        if self.winnable([]) is not winnable_mem([]):
            print("error 1 in winnable_mem")
        if self.winnable([0]) is not winnable_mem([0]):
            print("error 1 in winnable_mem")
        if self.winnable([0, 0]) is not winnable_mem([0, 0]):
            print("error 1 in winnable_mem")

        # Q 2

        # a
        if legal_path([[1, 0], [0, 1]], []) is not True:
            print("error 1 in legal_path")
        
        # c
        for i in range(1, 10):
            for p in range(300):
                A = [[choice([0, 1]) for l in range(i)] for k in range(i)]
                s = randint(0, i - 1)
                t = randint(0, i - 1)
                k = randint(1, 7)
                if self.path_v1(A, s, t, k) is not path_v2(A, s, t, k):
                    print("error in path_v2: A:", A, "s, t, k:", s, t, k)
            A = [[0 for l in range(i)] for k in range(i)]
            s = randint(0, i - 1)
            t = randint(0, i - 1)
            k = randint(1, 7)
            if self.path_v1(A, s, t, k) is not path_v2(A, s, t, k):
                print("error in path_v2: A:", A, "s, t, k:", s, t, k)

        if path_v2([[0,1,1,0,0], [1,0,1,0,0], [0,0,0,1,0], [1,0,0,0,0],[0,0,0,0,0]], 0, 4, 3):
            print("error 1 in path_v2")
        if not path_v2([[0,1,1,0,0], [1,0,1,0,0], [0,0,0,1,0], [1,0,0,0,0],[0,0,0,0,0]], 0, 3, 3):
            print("error 2 in path_v2")

        # d i
        try:
            self.path_v3(path_v3_b[0], path_v3_b[1], path_v3_b[2])
            print("error 1 in path_v3")
        except:
            pass # Greate.
        if not self.path_v3(path_v3_c[0], path_v3_c[1], path_v3_c[2]):
            print("error 2 in path_v3")
        try:
            self.path_v3(path_v3_d[0], path_v3_d[1], path_v3_d[2])
            print("error 1 in path_v3")
        except:
            pass # Greate.

        # d ii
        if not path_v3([[0, 1, 0], [1, 0, 1], [1, 1, 0]], 0, 2):
            print("error 1 in path_v3")
        if path_v3([[0, 1, 0], [1, 0, 0], [1, 1, 0]], 0, 2):
            print("error 2 in path_v3")

        for i in range(10000):
            size = randint(2, 9)
            k = randint(1, 12)
            C = [[0 for i in range(size)] for j in range(size)]
            for j in range(size):
                for i in range(size):
                    if i == j:
                        continue
                    C[j][i] = randint(0, 1)
            start = randint(0, size - 1)
            prev = start
            for i in range(k):
                available = list(range(size))
                available.remove(prev)
                next_point = choice(available)
                C[prev][next_point] = 1
                prev = next_point
            target = next_point
            B = deepcopy(C)
            if not path_v2(B, start, target, k):
                print("error 1 in path_v2. A:", B, start, target, k)
            if not path_v3(B, start, target):
                print("error 1 in path_v3. A:", B, start, target)

        # Q 3

        # a
        if can_create_once(7, [5, 2, 3]):
            print("error 1 in can create once.")
        if not can_create_once(6, [5, 2, 3]):
            print("error 2 in can create once.")
        if not can_create_once(0, []):
            print("error 3 in can create once.")
        if can_create_once(0, [5, 2, 9]):
            print("error 4 in can create once.")

        # b
        if not can_create_twice(7, [5, 2, 3]):
            print("error 1 in can create twice.")
        if not can_create_twice(6, [5, 2, 3]):
            print("error 2 in can create twice.")
        if not can_create_twice(0, []):
            print("error 3 in can create twice.")
        if not can_create_twice(0, [60, 2, 9]):
            print("error 4 in can create twice.")
        if not can_create_twice(-142, [60, 2, 9]):
            print("error 5 in can create twice.")
        if not can_create_twice(142, [60, 2, 9]):
            print("error 6 in can create twice.")
        if not can_create_twice(-142, [60, 2, 9]):
            print("error 7 in can create twice.")
        if can_create_twice(-99, [200, 2, 9]):
            print("error 8 in can create twice.")

        # c
        if not valid_braces_placement(10, [6, '-', 4, '*', 2, '+', 3]):
            print("error 1 in valid_braces_placement")
        if not valid_braces_placement(1, [6, '-', 4, '*', 2, '+', 3]):
            print("error 2 in valid_braces_placement")

        # Q 4

        # a
        if not grid_escape1([[1, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 1, 2]]):
            print("error 1 in grid escape 1")
        if grid_escape1([[2, 3, 1, 2], [2, 2, 2, 2], [2, 2, 3, 2], [2, 2, 2, 2]]):
            print("error 2 in grid escape 1")

        # b
        if not grid_escape2([[1, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 1, 2]]):
            print("error 1 in grid escape 2")
        if not grid_escape2([[2, 3, 1, 2], [2, 2, 2, 2], [2, 2, 3, 2], [2, 2, 2, 2]]):
            print("error 2 in grid escape 2")
        if grid_escape2([[2, 1, 2, 1], [1, 2, 1, 1], [2, 2, 2, 2], [4, 4, 4, 4]]):
            print("error 3 in grid escape 2")

    def change_v2_check_results(self, results, expected):
        """
            check if all the combinations in results are in expected and vice versa.
        """

        for comb in results:
            if comb not in expected:
                print("change_v2 error 1: results:", results, "expected:", expected)
                break
        for exp in expected:
            if exp not in results:
                print("change_v2 error 2: results:", results, "expected:", expected)
                break

    def winnable(self, board, show=False):
        """ determines if in a given configuration, represented by board, the player who makes the current move can force a win.
            board[i] is the height of column i
            show: if True and the configuration can force win, a possible move printed.
            This function is correct, check if the implemented one produces the same results.
        """
        
        if sum(board)==0: # halting after the (losing) move (0,0)
            return True 

        m = len(board)
        
        for i in range(m):  # for every column i
            for j in range(board[i]): # for every possible cell (i,j)
                # generate new munched board
                munched_board = board[0:i] + [min(board[k], j) for k in range(i,m)]

                # recursion
                if not self.winnable(munched_board):  # if munched board is losing
                    if show:                
                        print("recommended move:", board, "-->", munched_board) 
                    return True             

        return False # current board cannot force win

    def path_v1(self, A, s, t, k):
        """
            A correct solution to the problem.
        """
        
        if k == 0:
            return s == t
        for i in range(len(A)):
            if A[s][i] == 1:
                if self.path_v1(A, i, t, k-1):
                    return True
        return False

    def path_v3(self, A, s, t):
        if s == t:
            return True

        for i in range(len(A)):
            if A[s][i] == 1:
                if self.path_v3(A, i, t):
                    return True
        return False

print("running tests...")
my_tester = MyTest()
my_tester.test()
#test()
print("done.")
