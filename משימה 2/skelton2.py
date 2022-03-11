# Skeleton file for HW2 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.
# you can add new functions if needed.

# Change the name of the file to include your ID number (hw2_ID.py).
import random # loads python's random module in order to use random.random() in question 2

##############
# QUESTION 1 #
##############
#  Q1a
def divisors(n):
    pass  # replace with your code


#  Q1b
def perfect_numbers(n):
    pass  # replace with your code


#  Q1c
def abundant_density(n):
    pass  # replace with your code


#  Q1e
def semi_perfect_4(n):
    pass  # replace with your code

##############
# QUESTION 2 #
##############
# Q2a
def coin():
    pass  # replace with your code


# Q2b
def roll_dice(d):
    pass  # replace with your code


# Q2c
def roulette(bet_size, parity):
    pass  # replace with your code


# Q2d
def roulette_repeat(bet_size, n):
    pass  # replace with your code


# Q2e
def shuffle_list(lst):
    pass  # replace with your code


##############
# QUESTION 3 #
##############
# Q3a
def inc(binary):
    pass  # replace with your code


# Q3b
def pad_rev_lists(bin1, bin2):
    pass  # replace with your code


def add(bin1, bin2):
    pass  # replace with your code


# Q3c
def pow_two(binary, power):
    pass  # replace with your code


# Q3d
def div_two(binary, power):
    pass  # replace with your code


# Q3e
def leq(bin1, bin2):
    pass  # replace with your code


# Q3f
def to_decimal(binary):
    pass  # replace with your code


##############
# QUESTION 4 #
##############
# Q4a
def lychrel_loops(n):
    pass  # replace with your code


# Q4b
def is_lychrel_suspect(n, t):
    pass  # replace with your code


# Q4c
def lychrel_sort(numbers, t):
    pass  # replace with your code


##############
# QUESTION 5 #
##############
# Q5a
def calculate_grades_v1(grades):
    pass  # replace with your code

# Q5b
def calculate_grades_v2(grades, w, f):
    pass  # replace with your code

# Q5c_i
def calculate_grades_v3(grades, w):
    pass  # replace with your code

# Q5c_ii
def calculate_w(grades, target_average):
    pass  # replace with your code


##########
# Tester #
##########

def test():
    if divisors(6) != [1, 2, 3] or divisors(7) != [1]:
        print("Error in Q1a")

    if perfect_numbers(2) != [6, 28]:
        print("Error in Q1b")

    if abundant_density(20) != 0.15:
        print("Error in Q1c")

    if not semi_perfect_4(20) or semi_perfect_4(28):
        print("Error in Q1e")

    for i in range(10):
        if coin() not in {True, False}:
            print("Error in Q2a")
            break

    for i in range(10):
        if roll_dice(6) not in {1, 2, 3, 4, 5, 6}:
            print("Error in Q2b")
            break

    for i in range(10):
        if (roulette(100, "even") not in {0, 200}) or (roulette(100, "odd") not in {0, 200}):
            print("Error in Q2c")
            break

    shuffled_list = shuffle_list([1, 2, 3, 4])
    for i in range(1, 5):
        if i not in shuffled_list:
            print("Error in Q2e")
            break

    if inc("0") != "1" or \
            inc("1") != "10" or \
            inc("101") != "110" or \
            inc("111") != "1000" or \
            inc(inc("111")) != "1001":
        print("Error in Q3a")

    if add("0", "1") != "1" or \
            add("1", "1") != "10" or \
            add("110", "11") != "1001" or \
            add("111", "111") != "1110":
        print("Error in Q3b")

    if pow_two("10", 2) != "1000" or \
            pow_two("111", 3) != "111000" or \
            pow_two("101", 1) != "1010":
        print("Error in Q3c")

    if div_two("10", 1) != "1" or \
            div_two("101", 1) != "10" or \
            div_two("1010", 2) != "10" or \
            div_two("101010", 3) != "101":
        print("Error in Q3d")

    if not leq("1010", "1010") or \
            leq("1010", "0") or \
            leq("1011", "1010"):
        print("Error in Q3e")

    if lychrel_loops(28) != 2 or lychrel_loops(110) != 1:
        print("Error in Q4a")

    if (not is_lychrel_suspect(28, 1)) or is_lychrel_suspect(28, 2) or is_lychrel_suspect(28, 3):
        print("Error in Q4b")

    if lychrel_sort([165, 164, 28, 110, 196], 8) != [110, 28, 165, 164, 196]:
        print("Error in Q4c")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    if calculate_grades_v1(grades) != [95, 90.4]:
        print("Error in Q5a")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    w = 0.7
    f = lambda x: min(100, x + 3)
    if calculate_grades_v2(grades, w, f) != [95.6, 93.3]:
        print("Error in Q5b")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    w = 0.7
    if calculate_grades_v3(grades, w) != [94.25, 91.8]:
        print("Error in Q5c_i")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    target_average = 93.025  # This is the average of [94.25, 91.8]
    if abs(calculate_w(grades, target_average) - 0.7) > 0.000001:
        print("Error in Q5c_ii")
