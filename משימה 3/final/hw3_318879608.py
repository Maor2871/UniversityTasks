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
        fraction += int(octal[i]) * 8 ** (-i - 1)

    # That's it, return the fraction.
    return fraction        


# Q2 - G
oct_to_float = lambda octal: 0 if octal == '0000000000000000' else ((-1)**int(octal[0])) * 8**(((int(octal[1])*64 + int(octal[2])*8 + int(octal[3]))) - 255) * (1 + 7 * oct_to_fraction(octal[4:]))


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

        Question Notes:
            - The way of solving this problem is defintly mathematical and any other aprroach is difinitely out of place.
              Nevertheless, the question requirements state that using sqrt or rasing to the power of 0.5 is not allowed, therefore I will take it as a line which was meant to block mathematic approach.
              (There might be some math workarounds to the sqrt issue but i will take this obligation as an order to neglect any mathematic solution to this problem)
            - I will raise to a power of two though, in order to check if reached a valid approximation. I assume that it's allowed, because guessing the right number to square is the purpose of the sqrt obligation (so it seems).
            - x cannot be 0, because it is positive.

        Algorithm Notes:
            - A search for a very specific and accurate value to square requires a very good searching algorithm, so i will search a lion in the desert for that.
            - The left border is clearly the previous element in the series a1, ..., an. The right element cannot be tracked mathematically though. we want to determine the right border as quick as possible, because we are
              searching in the vast infinity in that case. Therefore we will use exponential expression to cut that chase to the right border as quick as possible.
            - We want the base of the exponent to be very big, but perhaps not too big on the beginnig and not too small if we have done several iterations already and the numbers climbed high.
              The last number found in the series is the perfect candidate for that.
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

        # --- Right border calculations (cut the chase in infinity exponentially) ---
        
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

        # --- Accurate element searching (lion in the desert) ---
        
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
    """
        The function receives an almost ordered list and an element. If the element is not in the list, returns None, otherwise returns its index.
    """

    # Search a lion in the desert.
    # Set the left and right borders (indices).
    left = 0
    right = len(lst) - 1

    # Narrow the desert.
    while right - left > 3:
        
        # The middle of the desert.
        middle = left + ((right - left) // 2)

        # Greater than the middle, can be middle - 1 though.
        if s >= lst[middle]:
            left = middle - 1

        # Less than the middle, can be middle + 1 though.
        if s <= lst[middle]:
            right = middle + 1

    # We closed on the desert, it has no more than 4 suspected elements.
    for i in range(left, right + 1):
        if s == lst[i]:
            return i

    # s is not in the list.
    return None


# Q4 - B
def sort_from_almost(lst):
    """
        The function receives an almost sorted list and  sorts it with in-place algorithm.
        Based on bubble sort.
    """

    # Iterate over the received list.
    for i in range(1, len(lst)):

        # Not good.
        if lst[i - 1] > lst[i]:

            # Replace.
            lst[i], lst[i -1 ] = lst[i - 1], lst[i]

    # The list is now ordered.
    return lst


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


def compute_median(q_l, q_g, k, n):
    """
        The function receives two qeury functions: query lower, query greater.
        It also receives a natural number k that represents the values range in the list, and a number n which represents the length of the list.
        The function returns the median in the list.
    """

    # The numbers in the list are between 0 and k inclusive. Search for the median like a lion in the desert.
    right = k
    left = 0

    # There must be a median inside the list.
    while True:
        
        # The middle rounded down.
        middle = left + (right - left)//2
        
        # The current middle is lower than too many numbers, it can't be the median.
        if q_g(middle) > n // 2:
            
            left = middle

        # The curent middle is greater than too many numbers, it can't be the median.
        elif q_l(middle) > n // 2:

            right = middle

        # The current middle is not greater and not lower than too many numbers, all the rest are equal to it. That's the median.
        else:
            return middle


# Q5 - A
def string_to_int(s):
    """
        The function receives a string of length k and returns the lexicographic place of the string in the 5 letters alphabet.
        Note:
            - The function is injective in relation to the length of the string (as noted in the requirements).
              Therefore, 'aaab' and 'ab' share the same value and it's valid.
    """
    
    # Calculate the place of the string during the iterations.
    place = 0

    # Alphabetic order.
    alphabetic_order = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
  
    # Iterate over the received string.
    for i in range(len(s)):

        # letter * (5 ** slot in s). Slot is from 0 to len(s) - 1 (right to left).
        place += alphabetic_order[s[i]]*(5**(len(s)- i - 1))

    return place



# Q5 - B
def int_to_string(k, n):
    """
        The function receives a place in the lexicographic dictionary, and returns the string in length k in that place.
    """

    # Alphabetic order.
    alphabetic_order = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e"}

    # The word mathces to the length and lexicographic place.
    word = ""
    
    # Keep extracting the letters with meaning.
    while n > 0:

        # Calculate the next letter.
        word = alphabetic_order[(n % 5)] + word

        # Discard the letter from n.
        n = n // 5

    # Fill the void with 'a's.
    word = 'a' * (k - len(word)) + word
    
    # Return the word in that place.
    return word


# Q5 - C
def sort_strings1(lst, k):
    """
        The function receives a list with n strings, each string of length k. It returns a lexicographic sorted copy of the list. O(5**k) of memory and O(5**k + n*k) running time.
    """

    # Each index represents the place in the lexicographic dictionary from 0 to 5**k. Each value represents a counter. O(5**k).
    dictionary = [0 for i in range(5**k)]

    # Iterate over the list. O(n*k).
    for i in range(len(lst)):

        # Calculate the place of the current string in the lexicographic dictionary, and increase its counter.
        dictionary[string_to_int(lst[i])] += 1

    # Return an ordered list with all the strings in lst. O(5**k + n*k).
    return [int_to_string(k, i) for i in range(5**k) for j in range(dictionary[i])]


# Q5 - E
def sort_strings2(lst, k):
    """
        The function receives a list with n strings, each string of length k. It returns a lexicographic sorted copy of the list. O(k) of memory and O((5**k)*n*k*) running time.
    """

    # The sorted list.
    sorted_list = []
    
    # Iterate over the dictionary.
    for i in range(5**k):
       
        # Count how many strings matches the current lexicographic place in the dictionary.
        for string in lst:

            # That's the place of the current string.
            if string_to_int(string) == i:

                # Add it now to the sorted list. Keep searching the list, a copy of the current string may hide further in the received list.
                sorted_list.append(string)

    # Return the sorted list.
    return sorted_list
    


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
    k = 100000
    n = 100
    q_l, q_g = generate_queries(k, n)
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

    # Q2 - G
    if oct_to_float('0400621000000000') != 51.859375:
        print("error in oct_to_float")
    if oct_to_float('0000000000000000') != 0:
        print("error in oct_to_float")
    
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

    # Q4 - A
    for lst in [[3], [3, 2], [2, 3], [3, 4, 5], [4, 3, 5], [3, 5, 4], [1, 4, 6, 9], [4, 1, 9, 6], [2, 1, 3, 5, 4, 7, 6, 8, 9],
                [23, 15, 32, 35, 98, 38, 104, 111, 106], [23, 15, 32, 35, 98, 38, 104, 111], [15, 23, 35, 32, 98, 38, 104, 111, 106, 114, 119, 140, 121, 160, 150, 203, 209]]:
        for i in range(len(lst)):
            if find(lst, lst[i]) != i:
                print("find error. list:", lst, "element:", lst[i])

    if find([23, 15, 32, 35, 98, 38, 104, 111, 106], 5) != None:
        print("find error 1")
    if find([23, 15, 32, 35, 98, 38, 104, 111, 106], 96) != None:
        print("find error 2")
    if find([23, 15, 32, 35, 98, 38, 104, 111, 106], 109) != None:
        print("find error 3")
    if find([23, 15, 32, 35, 98, 38, 104, 111, 106], 555) != None:
        print("find error 4")

    # Q4 - B
    for lst in [[3], [3, 2], [2, 3], [3, 4, 5], [4, 3, 5], [3, 5, 4], [1, 4, 6, 9], [4, 1, 9, 6], [2, 1, 3, 5, 4, 7, 6, 8, 9], [2, 1, 3, 5, 4, 7, 6, 8, 9],
                [23, 15, 32, 35, 98, 38, 104, 111, 106], [23, 15, 32, 35, 98, 38, 104, 111], [15, 23, 35, 32, 98, 38, 104, 111, 106, 114, 119, 140, 121, 160, 150, 203, 209]]:
        if sorted(lst) != sort_from_almost(lst):
            print("sort from almost error. lst:", lst)

    # Q4 - C
    for n in range(1, 1003, 1):
        for k in [n//2 + 1, n, 2*n, n**2]:
            q_l, q_g = generate_queries(k, n)
            M = compute_median(q_l, q_g, k, n)
            if not (q_l(M) <= n / 2 and q_g(M) <= n /2):
                print("error in compute median. median found:", M, "list length:", n, "numbers range:", k)

    # Q5 - A
    if string_to_int("a") != 0:
        print("string to int error 1")
    if string_to_int("c") != 2:
        print("string to int error 2")
    if string_to_int("ab") != 1:
        print("string to int error 3")
    if string_to_int("ea") != 20:
        print("string to int error 4")

    # Q5 - B
    if int_to_string(1, 0) != "a":
        print("int to string error 1")
    if int_to_string(1, 4) != "e":
        print("int to string error 2")
    if int_to_string(2, 6) != "bb":
        print("int to string error 3")
    for k in range(1, 7):
        for i in range(5**k):
            if string_to_int(int_to_string(k, i)) != i:
                print("Problem with ", i)
    alphabet = ["a","b","c","d","e"]
    for item in alphabet:
        if int_to_string(1, string_to_int(item)) != item:
            print("Problem with ", item)
    lst = [x+y for x in alphabet for y in alphabet]
    for item in lst:
        if int_to_string(2, string_to_int(item)) != item:
            print("Problem with ", item)
    lst = [x+y+z for x in alphabet for y in alphabet for z in alphabet]
    for item in lst:
        if int_to_string(3, string_to_int(item)) != item:
            print("Problem with ", item)

    # Q5 - C
    lst = ["eeee", "aabd", "abda", "cdea", "aabd"]
    if sort_strings1(lst, 4) != ["aabd", "aabd", "abda", "cdea", "eeee"]:
        print("sort strings 1 error 1")
    if sort_strings1([], 9) != []:
        print("sort strings 1 error 2")
    if sort_strings2(lst, 4) != ["aabd", "aabd", "abda", "cdea", "eeee"]:
        print("sort strings 2 error 1")
    if sort_strings2([], 9) != []:
        print("sort strings 1 error 2")

