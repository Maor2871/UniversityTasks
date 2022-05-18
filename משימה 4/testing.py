from hw4_318879608 import *
from itertools import combinations_with_replacement as cwr
from itertools import permutations

# This hyper-tester is brought to you by Snir Fridman of Animo's Workshop and Jonathan Yerushalmi of JY.inc
# DISCLAIMER: The tester named Bester does not guarantee your success,
#             but hopefully it will improve your odds.


###########################
# New and improved Bester #
###########################

def main():
    print("Commencing native test")
    native_test()
    print("Native test over")
    print("Commencing Bester")
    bester()
    print("Bester over")
    test_Q1()
    test_Q2()
    test_Q3()
    print("If no other prints occurred during the run, that's cool!")
    print("For additional CS guides, https://www.youtube.com/watch?v=dQw4w9WgXcQ")


def test_Q1():
    def change(amount, coins):
        """code shown in class, not mine"""
        if amount == 0:
            return 1
        if coins == []:  # No need to check amount here
            return 0
        result = 0
        if coins[0] <= amount:
            result += change(amount - coins[0], coins)
        return result + change(amount, coins[1:])

    def generate_options(k):
        letters = [0, 1, 2, 3, 4]
        combis = cwr(letters, k)
        words = []
        for comb in combis:
            pers = permutations(comb)
            for per in pers:
                words.append(tuple(sorted(per, reverse=True)))
        words = set(words)
        return sorted(list(set(words)))

    def make_lists(options):
        return [list(option) for option in options]

    ## biet
    my_coins = [1, 2, 3, 4]

    assert change_v2(0, my_coins) == [[]]
    for num in range(10):
        options = change_v2(num, my_coins)

        assert len(options) == change(num, my_coins)

        for option in options:
            assert sum(option) == num

    ##munch
    options = make_lists(generate_options(5))
    my_results = [True, False, True, True, True, True, True, False, True, True, True, True, False, True, True, True,
                  False, True, True, False, True, True, True, False, True, True, False, True, True, True, True, True,
                  True, True, True, True, True, True, False, True, True, True, False, True, True, True, True, True,
                  True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True,
                  False, False, True, True, True, True, True, False, True, True, True, True, True, True, True, True,
                  True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                  True, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True,
                  True, True, True, True, True, True, True, True, True, True, True, True, True]
    for option, result in zip(options, my_results):
        assert winnable_mem(option) == result
    print('You passed the Q1')

def test_Q2():
    ##daled
    A = [[0] + [1] * 4, [1, 0] + [1] * 3, [1] * 2 + [0] + [1] * 2, [1] * 3 + [0, 1], [1] * 4 + [0]]
    assert path_v3(A, 3, 2)

    print('You passed the Q2')

def test_Q3():
    L = [2, '+', 1, '*', 2, '-', 100, ]
    assert not valid_braces_placement(-1, L)

    L = [-2, '+', 3, '+', 3]
    assert valid_braces_placement(4, L)

    example = [1]
    for i in range(1, 6):
        for num in range(1, i + 1):
            example.append('+')
            example.append(1)

        assert not valid_braces_placement(-1, example)
        example = [1]

    print('You passed the Q3')

def bester():
    # 2c
    path_matrix = [[0, 1, 1, 0, 0], [1, 0, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for i in range(4):
        for j in range(5):
            if path_v2(path_matrix, i, 4, j):
                print("error in path_v2 - problems with node 4")
    if not path_v2(path_matrix, 0, 3, 5):
        print("error in path_v2")

    zero_matrix_len = 10
    zero_matrix = [([0] * zero_matrix_len)] * zero_matrix_len
    for i in range(10):
        for j in range(10):
            if i == j:
                if not path_v2(zero_matrix, i, j, 0):
                    print("error in path_v2 - zero matrix with length 0 and same nodes returns False")
            else:
                if path_v2(zero_matrix, i, j, 0):
                    print("error in path_v2 - zero matrix with length 0 and different nodes returns True")
            for k in range(1, zero_matrix_len):
                if path_v2(zero_matrix, i, j, k):
                    print("error in path_v2 - zero matrix with length >0 returns False")

    # 2d

    if path_v3_a != None or \
            path_v3_b == None or \
            path_v3_c != None or \
            path_v3_d == None:
        print("error in question 2d - path_v3_i variables are wrong")

    if not path_v3([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0, 2) or \
            path_v3([[0, 1, 0], [1, 0, 0], [0, 0, 0]], 0, 2):
        print("error in path_v3 - custom examples turn wrong results")

    for i in range(10):
        for j in range(10):
            if i == j:
                if not path_v2(zero_matrix, i, j, 0):
                    print("error in path_v3 - zero matrix with length 0 and same nodes returns False")
            else:
                if path_v2(zero_matrix, i, j, 0):
                    print("error in path_v3 - zero matrix with length 0 and different nodes returns True")
            for k in range(1, zero_matrix_len):
                if path_v2(zero_matrix, i, j, k):
                    print("error in path_v3 - zero matrix with length >0 returns False")

    # 3b

    if not can_create_twice(0, [7, 12, 2]):
        print("error in can_create_twice - zero should always be possible to make")
    if can_create_twice(100, [1] * 10):
        print("error in can_create_twice - out of reach number reached")

    # 4a

    if grid_escape1([[0, 0], [0, 0]]):
        print("error in grid_escape1 - zero matrix returns True")

    # 4b

    B4 = [[3, 3, 5, 2, 4],
          [0, 0, 1, 1, 0],
          [2, 0, 1, 1, 2],
          [0, 1, 0, 2, 0],
          [0, 4, 5, 0, 0]]

    if grid_escape2([[0, 0], [0, 0]]):
        print("error in grid_escape2 - zero matrix returns True")
    if not grid_escape2(B4):
        print("error in grid_escape2 - custom input turns False")


#################
# Native Tester #
#################

def native_test():
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
    """
    if path_v3_a != None and not path_v3(path_v3_a[0], path_v3_a[1], path_v3_a[2]):
        print("error in path_v3 or with path_v3_a")

    if path_v3_b != None and not path_v3(path_v3_b[0], path_v3_b[1], path_v3_b[2]):
        print("error in path_v3 or with path_v3_b")

    if path_v3_c != None and path_v3(path_v3_c[0], path_v3_c[1], path_v3_c[2]):
        print("error in path_v3 or with path_v3_c")

    if path_v3_d != None and path_v3(path_v3_d[0], path_v3_d[1], path_v3_d[2]):
        print("error in path_v3 or with path_v3_d")
    """
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


if __name__ == '__main__':
    main()
