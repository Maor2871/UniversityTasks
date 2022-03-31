# Skeleton file for HW3 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).
import math
import random


# ----- Semi - Functions -----


def random_game():
    """
        The function plays a game. In each round of the game, the function picks randomly a number in [0, 1].
        The game ends when the sum of all the numbers is greater than 1.
        The function returns the amount of rounds which where played.

        Note:
            - In the question it was remarked to generate a random number in [0, 1], but it was remarked to use random.random as well.
              The function random.random generates a number in [0, 1). The process to fix the problem is pretty complicated and I believe it's not one of the purposes of the question,
              so I chose to ignore the tiny mismatch, hopefully, it is understandable. (It is very unlikly to generate exactly 1 anyway).
    """

    # The total sum of all the picked random numbers.
    total_sum = 0

    # Count the number of rounds.
    rounds_counter = 0

    # Play the rounds, until the game is over.
    while total_sum < 1:

        # Pick a number and add it to the total.
        total_sum += random.random()

        # One more round was played.
        rounds_counter += 1

    # Return the amount of rounds played.
    return rounds_counter
        


# ----- Questions Implementations -----


# Q2 - F
def oct_to_fraction(octal):
    """
        The funciton receives an octal fraction as a 12 digits string, each digit is from 0 to 7 included.
        It returns the fraction id decimal. A number in [0,1).
    """

    # The total fraction.
    fraction = 0

    # Iterate over the digits.
    for i in range(len(octal)):

        # Add [digit * (1 / digit index)] to the final fraction sum.
        fraction += int(octal[i]) * 8**(-i - 1)

    # That's it, return the fraction.
    return fraction        


# Q2 - G
oct_to_float = lambda octal: ((-1)**int(octal[0])) * 8**(((int(octal[1])*64 + int(octal[2])*8 + int(octal[3]))) - 255) * (1 + 7 * oct_to_fraction(octal[4:]))


# Q2 - H
def is_greater_equal(oct1, oct2):
    """
        The function receives two octal numbers.
        It returns True if the first one is greater or equal to the second.
    """

    # Check if their signs are different (If they are, as long as numbers are not both 0, the positive one is greater than the negative).
    if oct1[0] != oct2[0]:

        # Make sure they are not both 0 (Note that checking if they are 0 with different signs only!).
        for i in range(1, 16):

            # One of the numbers is not 0, therefore they are not both 0.
            if oct1[i] != 0 or oct2[i] != 0:

                # True if oct1 is positive and oct2 is negative. Otherwise, False.
                return oct1[0] == "0"

        # Both numbers 0 indeed. The first number is indeed greater than or equal to the second.
        return True        
   
    # Iterate over the digits of the numbers.
    # The fractions are relevant only if the exponents are the same, therefor it would be accurate to check the digits in left to right order.
    # The first pair of different digits determines which number is greater in absolute value. 
    for i in range(1, 16):

        # Different digits found.
        if oct1[i] != oct2[i]:

            # The first number is greater in absolute value.
            if int(oct1[i]) > int(oct2[i]):

                # The numbers are positive.
                if oct1[0] == "0":

                    # The first one is greater.
                    return True

                # The numbers are negative, therefore the second one is greater.
                return False

            # The second number is greater in absolute value.
            else:

                # The numbers are positive.
                if oct1[0] == "0":

                    # The second one is greater.
                    return False

                # The numbers are negative, therefore the first one is greater.
                return True

    # Exactly the same.
    return True
                

# Q3 - A
def approx_root(x, eps):
    """
        The function recieves a positive real number, x, and epsilon > 0.
        It calculates the approximation of sqrt x up to epsilon, with the aprroach described in the question.
        It returns the series a1, ..., an, and the final approximation value.

        Notes:
            - The way of solving this problem is defintly mathematical and any other aprroach is difinitely out of place.
              Nevertheless, the question requirements state that using sqrt or rasing to the power of 0.5 is not allowed, therefore I will take it as a line which was meant to block mathematic approach.
              (There may be math workarounds to the sqrt issue but i will take this obligation as an order to neglect any mathematic solution to this problem)
            - I will raise to a power of two though, in order to check if reached a valid approximation. I assume that it's allowed, because guessing the right number to square is the purpose of the sqrt obligation (so it seems).
            - A search for a very specific and accurate value to square requires a very good searching algorithm, so i will search a lion in the desert for that.
            - The left border is clearly the previous element in the series a1, ..., an. The right element cannot be tracked mathematically though. we want to determine the right border as quick as possible, because we are
              searching in the vast infinity in that case. Therefore we will use exponential expression to cut that chase to the right border as quick as possible.
            - We want the base of the exponent to be very big, but perhaps not too big on the beginnig and not too small if we have done several iterations already and the numbers climbed high.
              The last number found in the series is the perfect candidate for that.
            - x cannot be 0, because it is positive.
    """

    # The current approximation value. After the loop will contain the final solution.
    approximation_value = 0

    # Document the numbers of the series a1, ..., an.
    series = []

    # Record the current multiplication of the series (a1*a2 *** an)
    series_multiplication = 1

    # Initialize the left border with 1, the lowest natural number.
    left_border = 1

    # The right border is calculated at the beginning of the loop, the required initial value is the left border.
    right_border = 1
    
    # Keep looping until a valid approximation is found.
    # Note that we cannot use sqrt. sqrt(x) - approx < eps  ↔  x < eps**2 + 2*approx*eps + approx**2
    while not x < eps**2 + 2*approximation_value*eps + approximation_value**2:

        # --- Right border calculations ---
        
        # The exponent.
        power_attempt = 1

        # Search the infinity by increasing the exponent each iteration.
        # Keep iterating until a small enough component is found.
        while (approximation_value + (1 / (series_multiplication * (right_border**power_attempt))))**2 > x:

            # Solves the deadlock of right_border = 1 is not enough. This step does not really affects the execution time or the algorithm.
            right_border += 1
            
            # The component is not small enough, increase the power.
            power_attempt += 1

        # We found the right border.
        right_border = right_border ** power_attempt

        # --- Accurate element searching ---
        
        # The accurate number is found when the approximation value squared will be the closest to x but smaller than x.
        while left_border != right_border:

            # Calculate the middle number, between the borders.
            middle = left_border + (right_border - left_border) // 2

            # The middle is valid, but not necessarily the minimal.
            if (approximation_value + (1 / (series_multiplication * middle)))**2 <= x:

                # Cut the right border.
                right_border = middle

            # The middle is not enough, we need a smaller component.
            else:

                # If True, then we reached a deadlock of right_border = left_border + 1 (div floors).
                if left_border == middle:

                    # The left border is one step too much, change to the right border.
                    left_border = right_border

                # There's still a way to go.
                else:

                    # Cut the left border.
                    left_border = middle
        
        # We found the most accurate component. Add it to the series.
        series.append(left_border)

        # Update the seiries multiplication.
        series_multiplication *= left_border

        # Update the approximation value.
        approximation_value += (1 / series_multiplication)

        # The left border in the search for the next element in the series, is the previous element, Therefore, its value is unchanged.
        # The right border is calculated at the beginning of the loop, and the initial value for the calculations is the left border, so its value is unchanged as well.

    # Done.
    return series, approximation_value

# Q3 - B
def approx_e(N):
    """
        The function recieves a natural number N and performs N rounds to the described random game in the question.
        It returns the average rounds it took to finish each game.
    """

    # Rounds counter of all the games.
    overall_rounds = 0

    # Play N games.
    for i in range(N):

        # Play the game, and add the number of rounds to the total rounds counter.
        overall_rounds += random_game()

    # Return the average amount of rounds played.
    return overall_rounds / N
	

# Q4 - A
def find(lst, s):
    pass  # replace this with your code


# Q4 - B
def sort_from_almost(lst):
    pass  # replace this with your code


# Q4 - C
def generate_queries(k = 100, n = 1000):
    L = []
    for i in range(n):
        L.append(random.randint(0, k-1))
    
    def q_g(m):
        size = 0
        for i in range(n): 
            if L[i]>m: size +=1
        return size
    
    def q_l(m):
        size = 0
        for i in range(n): 
            if L[i]<m: size +=1
        return size

    return q_l, q_g

k = 100000
n = 100
q_l, q_g = generate_queries(k, n)


def compute_median(q_l, q_g, k, n):
    pass  # replace this with your code


# Q5 - A
def string_to_int(s):
    pass  # replace this with your code


# Q5 - B
def int_to_string(k, n):
    pass  # replace this with your code


# Q5 - C
def sort_strings1(lst, k):
    pass  # replace this with your code


# Q5 - E
def sort_strings2(lst, k):
    pass  # replace this with your code


##########
# Tester #
##########
def test():
    # Q2 - C
    if oct_to_fraction('621000000000') != 0.783203125 or oct_to_fraction('202200000000') != 0.25439453125:
        print('error in oct_to_fraction')
    # Q2 - D
    if oct_to_float('0400621000000000') != 51.859375:
        print("error in bin_to_float")
    # Q2 - E
    if is_greater_equal('0401010000000000', '0400010000000000') == False or \
       is_greater_equal('0400007777777777', '0400010000000000') == True:
        print("error in is_greater_equal")
    # Q3 - A
    if approx_root(2, 0.1) != ([1, 3], 1 + 1/3):
        print("error in approx_root (1)")
    if approx_root(2, 0.02) != ([1, 3, 5], 1 + 1/3 + 1/15):
        print("error in approx_root (2)")
    if approx_root(2, 0.001) != ([1, 3, 5, 5], 1 + 1/3 + 1/15 + 1/75):
        print("error in approx_root (3)")
    # Q3 - B
    if abs(approx_e(1000000) - math.e) > 0.01:
        print("MOST LIKELY there's an error in approx_e (this is a probabilistic test)")

    # Q4 - A
    almost_sorted_lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]
    if find(almost_sorted_lst, 5) != 3:
        print("error in find")
    if find(almost_sorted_lst, 50) != None:
        print("error in find")
    
    # Q4 - B
    if sort_from_almost(almost_sorted_lst) != sorted(almost_sorted_lst):
        print("error in sort_from_almost")
    
    # Q4 - C
    M = compute_median(q_l, q_g, k, n)
    if not ((q_l(M) <= n//2) and (q_g(M) <= n//2)):
        print("error in compute_median")
    
    # Q5
    lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
    for i in lst_num:
        s = int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if string_to_int(s) != i:
            print("error in int_to_string and/or in string_to_int")

    lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
    if sort_strings1(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings1")

    if sort_strings2(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings2")

def my_test():
    """
        Test the code.
    """

    # Q2 - F
    if oct_to_fraction("000000000000") != 0:
        print("oct_to_fraction error 1")

    # Q2 - H
    if not is_greater_equal("0000000000000000", "0000000000000000") == True:
        print("is_greater_equal error 1")
    if not is_greater_equal("1000000000020000", "0000000000000000") == False:
        print("is_greater_equal error 2")
    if not is_greater_equal("0000000000000000", "1000000000400000") == True:
        print("is_greater_equal error 3")
    if not is_greater_equal("1000000000000000", "0000000000000003") == False:
        print("is_greater_equal error 4")
    if not is_greater_equal("0000000000000200", "1000000000000000") == True:
        print("is_greater_equal error 5")
    if not is_greater_equal("0000000000000200", "0000000000000000") == True:
        print("is_greater_equal error 6")
    if not is_greater_equal("0003000000000200", "0000000000005000") == True:
        print("is_greater_equal error 7")
    if not is_greater_equal("1000000005000000", "1000000000000700") == False:
        print("is_greater_equal error 8")
    if not is_greater_equal("1000400005000030", "1000400005000030") == True:
        print("is_greater_equal error 9")

    # Q3 - A
    if not approx_root(4, 0.5) == ([1, 1], 2):
        print("approx_root error 1")
    if not approx_root(6.25, 0.5) == ([1, 1, 2], 2.5):
        print("approx_root error 2")
    if not approx_root(7.6176, 0.001) == ([1, 1, 2, 2, 25], 2.76):
        print("approx_root error 3")
    if not approx_root(0.25, 0.001) == ([2], 0.5):
        print("approx_root error 4")
    if not approx_root(2, 0.0001) == ([1, 3, 5, 5, 16], 1.4141666666666666):
        print("approx_root error 5")
    if not approx_root(0.111111777, 0.00000000001) == ([3, 333724], 0.3333343321627053):
        print("approx_root error 6")
    if not approx_root(0.0000000500036, 0.00000000000001) == ([4472, 178642], 0.0002236148474480667):
        print("approx_root error 7")
    if not approx_root(4.000001, 0.0000000000001) == ([1, 1, 4000001], 2.0000002499999376):
        print("approx_root error 8")
    if not approx_root(12.94373064, 0.00000000000001) == ([1, 1, 1, 2, 6, 6, 27, 170, 536, 5577], 3.5977396570624727):
        print("approx_root error 9")

    # Q3 - B
    if not 2.5 < approx_e(50000) < 3:
        print("approx_e failed to generate e on a very unlikely occasion")
    
#test()
print()
print("running my tests:")
my_test()
print("done")
