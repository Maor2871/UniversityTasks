# Skeleton file for HW3 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).
import math
import random

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
    pass  # replace this with your code


# Q3 - B
def approx_e(N):
    pass  # replace this with your code
	

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
    
test()
print()
print("running my tests:")
my_test()
print("done")
