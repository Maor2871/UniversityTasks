# Skeleton file for HW2 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.
# you can add new functions if needed.

# Change the name of the file to include your ID number (hw2_ID.py).

import random # loads python's random module in order to use random.random() in question 2
from time import perf_counter


#----- Semi Functions -----


def is_perfect_number(n):
    """
        The function receives a number and returns True if it is a perfect number, Otherwise returns False.
        An perfect number is a number which the sum of its divisors equals itself.
    """

    # Sum the divisors of the received number and check if the sum is equal to the number itself.
    # Note that in proportions to the list of divisors, the iterations over 1-n is way longer than the iteration of sum on the list of divisors.
    return sum(divisors(n)) == n


def is_abundant_number(n):
    """
        The function receives a number, it returns True if it is an abundant number, otherwise returns False.
        An abundant number is a number which the sum of its divisors > itself.
    """

    return sum(divisors(n)) > n


def pad_binaries(bin1, bin2):
    """
        The function recieves to binary numbers as strings.
        It finds the longer number, and pads 0 to the left of the shorter one so that they will be equally lengtht.
    """

    if len(bin1) > len(bin2):

        return bin1, "0" * (len(bin1) - len(bin2)) + bin2

    return "0" * (len(bin2) - len(bin1)) + bin1, bin2


def lychrel_loops_limit(n, limit):
    """
        The function receives a number n and a limit.
        It returns False, count if the number is not limit lychrel suspect, where count is the amount of rounds required.
        Otherwise, return True, 0.
    """

    # The rounds counter.
    count = 0

    # Keep on iterating. When step 3 in the algorithm is True, break.
    for i in range(limit):

        # Start a new round.
        count += 1
        
        # Calculate the reversed form of the number.
        reversed_n = int(str(n)[::-1])

        # Update the number as described in step 2.
        n = n + reversed_n

        # Step 3 is True, the new number is a polyndrom.
        if str(n) == str(n)[::-1]:
            return False, count

    # the number is [limit] lychrel suspect.
    return True, 0

#----- Answers -----


##############
# QUESTION 1 #
##############


#  Q1a
def divisors(n):
    """
        The function receives a number and returns a list with all its divisors.
    """

    # Simply iterate over all the numbers in {1, ..., n-1} and save by order those which divides n.
    return [current_num for current_num in range(1, n) if n/current_num - int(n/current_num) == 0]
    

#  Q1b
def perfect_numbers(n):
    """
        The function receives a number n, and returns the first n prefect numbers.
        A perfect number n, is a number which has n divisors.
        Note: Following the example in the question, it is concluded that 1 is not considered to be a perfect number.
    """
    
    # A list which will contain at the end of the while loop, all the first n perfect numbers.
    first_perfect_numbers = []

    # The current number that the following loops checks.
    current_number = 2
    
    # Keep iterating over natural numbers, until collected enough perfect numbers.
    while len(first_perfect_numbers) < n:

        # Check if the current number has [current_number] divisors.
        if is_perfect_number(current_number):

            # The current number is a perfect number, save it.
            first_perfect_numbers.append(current_number)

        # Move the the next natural number to check.
        current_number += 1

    # Return the list of the first n perfect numbers.
    return first_perfect_numbers
    

#  Q1c
def abundant_density(n):
    """
        The function receives a number n and finds all the abundant numbers up to n.
        It then calculates the density of those numbers and returns it.
    """

    # A conter of all the abundant numbers up to n.
    abundant_numbers_counter = 0
    
    # Iterate over all the numbers up to the received n.
    for current_num in range(1, n + 1):

        # Check if the current number is an abundant number.
        if is_abundant_number(current_num):

            # Increate the counter by 1.
            abundant_numbers_counter += 1
            
    # Now, calculate the density of all the abundant numbers up to n.
    # The density is simply the ratio of abundant numbers vs. all numbers up to n.
    return abundant_numbers_counter / n


#  Q1e
def semi_perfect_4(n):
    """
        The function receives a number and returns True if the number is a semi-perfect number of 4th order.
    """

    # Extract the divisors of n.
    n_divisors = divisors(n)
   
    # Those are the divisors that haven't been fully tested yet.
    divisors_to_check_1 = n_divisors.copy()
   
    # Iterate over all the combinations of different four divisors of n.
    # Do so by each iteration excluding the divisors which were already tested.
    # This way, make sure not to test twice the same combination.
    for first in n_divisors:

        # No need to check the current divisor, not at the current nested loops iteration,
        # and not at the nested loops of the following iterations.
        divisors_to_check_1.remove(first)

        # Those are the divisors that haven't been fully tested yet with the current first divisor. 
        divisors_to_check_2 = divisors_to_check_1.copy()

        # Keep on iterating over the divisors which haven't been tested yet.
        for second in divisors_to_check_1:

            # Exlude those which were already tested and prepare the excluding list for the third nested loop.
            divisors_to_check_2.remove(second)
            divisors_to_check_3 = divisors_to_check_2.copy()          

            # Get the third divisor.
            for third in divisors_to_check_2:

                # And exclude.
                divisors_to_check_3.remove(third)

               # Get the fourth divisor.
                for fourth in divisors_to_check_3:

                    # Now check if the current four chosen divisors sums up to the received n.
                    if first + second + third + fourth == n:

                        # It is a semi-perfect number of 4th order.
                        return True

    # No combination of 4 divisors sums to n founded. n is not a semi-perfect number.
    return False


##############
# QUESTION 2 #
##############


# Q2a
def coin():
    """
        The function flips a coin. It returns True if heads, False if tails.
    """

    # random.random() returns a number n such that, 0.0 <= n < 1.
    # Therefore, to have the exactly same chances, i.e 50%, split into [0, 0.5) and [0.5, 1).
    if random.random() >= 0.5:
        return True
    return False


# Q2b
def roll_dice(d):
    """
        The function receives a size of an equal dice, and rolls the correct dice. It returns the chosen number.
        Note that d is a natural number and greater than or equal to 2.
        Note that the function returns a number in {1, 2, ..., d}, because each one of these number represents a side of the dice. 
    """

    # Get a random number, 0 <= n < 1.
    random_num = random.random()

    # if [0 <= random_num < 1/d], then [0 <= d * random_num < 1] - so returns 0 + 1 = 1.
    # if [1/d <= random_num < 2/d], then [1 <= d * random_num < 2] - returns 1 + 1 = 2.
    # and so on... up to:
    # if [(d-1)/d <= random_num < 1], then [d-1 <= d * random_num < d] - returns d-1 + 1 = d.
    # Therefore each number from 1 to d included, has the same chance of getting chosen.
    return int(random_num * d) + 1


# Q2c
def roulette(bet_size, parity):
    """
        The function receives a bet size as an integer and a parity flag as a string: "even"/"odd".
        The function chooses a number in {0, 1, ..., 36} at equal chances.
        If 0 was chosen, returns 0.
        If a number which its parity matches the received parity, doubles the bet size and returns it.
        Otherwise, returns 0.
    """

    # Map the parity from string to int.
    parity = {"even": 0, "odd": 1}[parity]
    
    # Get a number in {0, 1, 2, ..., 36}.
    roulette_result = roll_dice(37) - 1
    
    # With such a bad luck, you really shouldn't be gambling. Got 0 out of 36.
    if roulette_result == 0:
        return 0

    # Horray! The parity received and the parity of the chosen number matches!
    elif roulette_result % 2 == parity:
        return 2 * bet_size

    # Ho no! no match in parities.
    return 0
    

# Q2d
def roulette_repeat(bet_size, n):
    """
        The function plays the roullete n times.
        It choses the parity flag by flipping a coin, therefore half a chance an odd bet, half a chance even.
        Note that the function chooses a new parity flag each round.
    """

    # Will contain the final financial balance after playing the roulette n times, with [bet_size] each round.
    final_balance = 0
    
    # Play the roulette n times.
    for i in range(n):

        # Flip a coin to choose the parity.
        parity = {True: "even", False: "odd"}[coin()]

        # Well, we have to pay the [bet_size] to play the roulette.
        # (reset current_round_balance from previous round on the way)
        current_round_balance = - bet_size
        
        # Now play the roulette with the received bet size and the chosen parity. Add the award to final balance.
        current_round_balance += roulette(bet_size, parity)

        # Add the balance of the current round to the final balance.
        final_balance += current_round_balance
 
    # This is it, return the final balance.
    return final_balance


# Q2e
def shuffle_list(lst):
    """
        The function receives a list and returns the list shuffled.
    """

    # The shuffled list.
    shuffled = []

    # Don't damage the original list.
    # Contains all the elements which haven't been chosen yet.
    elements_remained = lst.copy()
    
    # Pop all the n indexes of the received list (n is the length of the list).
    # Iterate over the length of the list, from the length to 1:
    # n, n-1, ..., 3, 2, 1.
    for current_length in range(len(lst), 0, -1):

        # Choose a random slot from the remains list.
        random_slot = roll_dice(current_length) - 1

        # Pop the element in the chosen slot from the remains list, and append it to the shuffled list.
        shuffled.append(elements_remained.pop(random_slot))

    # That's it. All the elements from the received list are now shuffled in shuffled.
    return shuffled


##############
# QUESTION 3 #
##############


# Q3a
def inc(binary):
    """
        the function receives a positive binary number as a string of '0' and '1'.
        It increments the number by 1 and returns the new number.
    """

    # If the first digit is 0 there is no carry and the new number is simply the received with 1 as the rightest digit.
    if binary[-1] == "0":
        return binary[:-1] + "1"

    # True if we carry 1 from the previous iteration.
    # Initial value is set to point on the status after the incrementation.
    # If reached this line, there was a carry.
    carry = True

    # Set the rightest digit of the new line to be 0, the carry flag is on.
    new_binary = "0"
    
    # Iterate over the digits of the binary number, from right to left and handle the carry.
    for i in range(1, len(binary)):

        # Extract the current digit.
        digit = binary[len(binary) - 1 - i]

        # Check if the current digit is 1 and we have a carry from privious iteration.
        if digit == "1" and carry:

            # Keep on carrying.
            continue

        # That's it, the incrementation process came to an end.
        else:

            # Concatinate 1's from the beginnig of the number to the current point, the new 1, and the rest of the number.
            return binary[: len(binary) - 1 - i] + "1" + "0" * (i)

    # If reached this point, the carry went on and on till the end of the number.
    # Therefore, the new number is of the form: "1 0 0 0, ..., 0".
    return "1" + "0" * len(binary)


# Q3b
def pad_rev_lists(bin1, bin2):
    """
        I find it confusing to reverse the lists, so i left the signature and created pad_binaries only.
    """

    return


def add(bin1, bin2):
    """
        The function receives two binary numbers and returns thier binary sum.
    """

    # Pad the shorter number with "0" to its left, so bin1, bin2 will be equally lengtht.
    bin1, bin2 = pad_binaries(bin1, bin2)

    # The binary sum of the two received numbers.
    binary_sum = ""

    # The length of the numbers.
    original_length = len(bin1)
    
    # Start with no carry.
    carry = False

    # Iterate over the digits of the two numbers from right to left.
    for i in range(0, original_length):

        # Extract the current digitits.
        digit1, digit2 = bin1[original_length - i - 1], bin2[original_length - i - 1]

        # Check if there is a carry from the previous iteration.
        if carry:

            # if we add 1 and 0 with carry, we get 0 with carry (simply keep carry on).
            if digit1 != digit2:

                binary_sum = "0" + binary_sum

            # If we add 1 and 1 with carry, we get 1 with carry (simply keep carry on).
            elif digit1 == digit2 and digit1 == "1":

                binary_sum = "1" + binary_sum

            # If we add 0 and 0 with carry we get 1 with no carry.
            else:

                binary_sum = "1" + binary_sum
                carry = False

        # There's no carry.
        else:

            # if we add 1 and 0, the sum is simply 1.
            if digit1 != digit2:
                
                binary_sum = "1" + binary_sum

            # If we add 0 and 0, the sum is 0.
            elif digit1 == digit2 and digit1 == "0":

                binary_sum = "0" + binary_sum

            # Otherwise we add 1 and 1.
            else:

                # Turn on the carry flag and concatinate 0 to the final sum.
                binary_sum = "0" + binary_sum

                carry = True

    # We finished the loop with carry. It means the length of the sum is greater than the components.
    if carry:

        binary_sum = "1" + binary_sum

    # This is it, return the binary sum.
    return binary_sum

# Q3c
def pow_two(binary, power):
    """
        The function recieves a binary number and a power.
        It returns the multiplication of the binary number and 2 to the received power.
        Algorithm:
            Note that a binary number can be represented as: Σ[Ak*(2**k)] (where k runs from 0 to the length of the number - 1 included, and Ak is a zero or a one).
            Therefore, if p is the recieved power, the calculation is Σ[Ak*(2**k)] * 2**p = Σ[Ak*(2**k)*(2**p)] = Σ[Ak*(2**(k+p))].
            Now because we are dealling with the binary base, it simply shifts left the number by p, and fills the void with only 0.
    """

    return binary + "0" * power


# Q3d
def div_two(binary, power):
    """
        The function receives a binary number and a power.
        It returns the division of the binary number and 2 to the received power.
        Algorithm:
            Suppose binary number is Σ[Ak*(2**k)]. Note that Σ[Ak*(2**k)] / (2**p) = Σ[Ak*(2**(k-p))].
            Now if we eventuall floor the received number, its as simple as ignoring those 2 power negtive numbers.
            Therefore, we are left with Σ[Ak*(2**(k-p))] for k >= p. Which simply means throw away all the digits from the right side of the number to the length - p - 1 digit.
    """

    # Nothing left from the number.
    if len(binary) <= power:
        return "0"

    # Cut the numbers from the right to the power_th digit included.
    return binary[:len(binary) - power]


# Q3e
def leq(bin1, bin2):
    """
        The function receives two binary numbers. It returns True if the first one is less than or equal to the second number. Otherwise returns False.
    """

    # Both bin1 and bin2 starts with a digit 1 from the left. Otherwise one of them is 0.
    # Therefore if bin1 is shorter than bin2, no need to check anything, it is less than bin2.
    if len(bin1) < len(bin2):
        return True

    # Same idea if the length of bin2 is shorter than of bin1.
    elif len(bin2) < len(bin1):
        return False

    # The two numbers share the same length. Iterate over their digits from left to right (Check the leftest digit either for the case in which their length is 1).
    for i in range(len(bin1)):

        # bin1 is less than bin2.
        if bin1[i] == "0" and bin2[i] == "1":
            return True

        # bin2 is less than bin1.
        elif bin2[i] == "0" and bin1[i] == "1":
            return False

        # Keep on checking.

    # The two numbers are simply the same, therefore, bin1 <= bin2.
    return True


# Q3f
def to_decimal(binary):
    """
        The function receives a binary number and returns its decimal value.
    """

    # The final decimal value of the received number.
    decimal_value = 0
    
    # Iterate over the digits of the received number from right to left.
    for i in range(len(binary)):

        # If the current digit is 1.
        if binary[-i - 1] == "1":

            # Add its value * 2 to the power of its index to the decimal value.
            decimal_value += 2 ** i

    # The sumed up decimal value is exactly the decimal value of the received binary number.
    return decimal_value
    

##############
# QUESTION 4 #
##############


# Q4a
def lychrel_loops(n):
    """
        The function receives a number and counts the number of rounds required to reach a polynom at the following algorithm:
        1. find the reversed number.
        2. update the number to be the sum of itself and its reversed self.
        3. check if the new number is a polyndrom.
    """

    # The rounds counter.
    count = 0

    # Keep on iterating. When step 3 in the algorithm is True, break.
    while True:

        # Start a new round.
        count += 1
        
        # Calculate the reversed form of the number.
        reversed_n = int(str(n)[::-1])

        # Update the number as described in step 2.
        n = n + reversed_n

        # Hooray. Step 3 is True, the new number is a polyndrom.
        if str(n) == str(n)[::-1]:
            break

    # Return the number of rounds it takes to reach a polyndrom.
    return count

# Q4b
def is_lychrel_suspect(n, t):
    """
        The function recieves a number n and an integer t. It returns True if the received number is t lychrel suspicious.
    """
   
    # Make t attemts.
    for i in range(t):
      
        # Calculate the reversed form of the number.
        reversed_n = int(str(n)[::-1])

        # Update the number as described in step 2.
        n = n + reversed_n

        # Step 3 is True, the new number is a polyndrom.
        # Therefore it is not a t lychrel suspicious number.
        if str(n) == str(n)[::-1]:
            return False           

    # The number did not reach a polyndrom form after t rounds. It is t lychrel suspicious indeed.
    return True
    

# Q4c
def lychrel_sort(numbers, t):
    """
        The function receives a list of numbers and and integer t.
        It returns a new list with all the numbers, only sorted by their lychrel suspect rounds quantity. The form of the list:
        [a, b, c, ..., d, e, f, ...]
        where a,b,c,... are numbers which are not t lychrel suspects, and ordered by their rounds quantity in ascending order (equal rounds --> original order).
        and d,e,f,... are numbers which are t lychrel suspects, and are ordered by their original order.
    """

    # Will eventualy contain all the t lychrel suspect numbers by order.
    t_lychrel_suspects_ordered = []

    # Will eventualy contain all the numbers which are not t lychrel suspects, ordered by their rounds, in ascending order.
    # If two numbers share the same amount of rounds, keep the order in the original numbers list.
    numbers_rounds_ordered = []

    # Iterate over the calculations by order and initiate the two lists, keep original order.
    for number in numbers:

        # Calculate the lychrel status of the current number, the results are (is_t_lychrel_suspect, rounds).
        # (F, count) indicates the number is not a t lychrel suspect and is a polyndrom after [count] rounds.
        # (T, 0) indicates the number is t lychrel suspect.
        is_t_lychrel_suspect, rounds = lychrel_loops_limit(number, t)

        # The current number is t lychrel suspect.
        if is_t_lychrel_suspect:
            t_lychrel_suspects_ordered.append(number)

        # The current number is not a t lychrel suspect, save the required amount of rounds.
        else:

            # numbers_rounds_ordered will be of the form [{"number": <number>, "rounds": <rounds>]}].
            # This form is nicely applicated later on with the sort method.
            numbers_rounds_ordered.append({"number": number, "rounds":rounds})

    # The t_lychrel_suspects_ordered list is ready.
    # Sort the numbers_rounds_ordered list by the number of rounds, keep the original order.
    numbers_rounds_ordered.sort(key=lambda number: number["rounds"])
    
    # Now combine the two lists to one, and return the new list.
    return [number["number"] for number in numbers_rounds_ordered] + t_lychrel_suspects_ordered


##############
# QUESTION 5 #
##############


# Q5a
def calculate_grades_v1(grades):
    """
        The function receives a grades list and returns the final grades list, at a matching order.
    """

    # A list with all the final grades of the students.
    final_grades = []
    
    # Iterate over the test and home-work grades of each student in the list.
    for test_grade, hw_grades in grades:

        # Calculate the average grade of the hw.
        final_hw_grade = sum(hw_grades) / 3

        # Check if the final hw grade is greater than the test grade.
        if final_hw_grade > test_grade:

            # Add the hw grade into calculations and save the final grade.
            final_grades.append(0.1 * final_hw_grade + 0.9 * test_grade)
        
        # The test grade is the final grade of the current studnet.
        else:
            final_grades.append(test_grade)

    # Return the list with the final grades.
    return final_grades

# Q5b
def calculate_grades_v2(grades, w, f):
    """
        The function receives a list of grades, a weight for the test, and a factor fanction.
        It calculates and returns the final grades of the students.
    """

    # A list with all the final grades of the students.
    final_grades = []

    # Iterate over the test and home-work grades of each student in the list.
    for test_grade, hw_grades in grades:

        # Calculate the final grade of the current student and save it in the final grades list.
        final_grades.append(w * f(test_grade) + (1 - w) * (sum(hw_grades) / 3))

    # Return the list with all the final grades of the students.
    return final_grades


# Q5c_i
def calculate_grades_v3(grades, w):

    # A list with all the final grades of the students.
    final_grades = []

    # Iterate over the test and home-work grades of each student in the list.
    for test_grade, hw_grades in grades:
       
        # Calculate the final grade of the current student and save it in the final grades list.
        final_grades.append(w * test_grade + (1 - w) * (sum(sorted(hw_grades[1:3])) / 2))

    return final_grades


# Q5c_ii
def calculate_w(grades, target_average):
    """
        The function receives a list with grades and a target average. It returns the w required to each that average.
        In case no w will create the desired average, returns None.
        The Calculation is very simple. Algorithm: (n - number of students)
            [Σ(w * test_gradeK + (1 - w) * hw_gradeK)] / n = target_avg
            Σ(w* test_gradeK) + Σ((1 - w) * hw_gradeK) = target_avg * n
            w * Σ(test_gradeK) + (1 - w) * Σ(hw_gradeK) = target_avg * n
            w * Σ(test_gradeK) + Σ(hw_gradeK) - w * Σ(hw_gradeK) = target_avg * n
            w * [Σ(test_gradeK) - Σ(hw_gradeK)] = target_avg * n - Σ(hw_gradeK)
            w = [target_avg * n - Σ(hw_gradeK)] / [Σ(test_gradeK) - Σ(hw_gradeK)]
    """  

    # --- Calculate data for the formula ---
    
    # Σ(test_gradeK), Σ(hw_gradeK).
    sum_test_grades = 0
    sum_hw_grades = 0
    
    # Calculate the sum of all the test grades and the sum of all the hw_grades.
    for test_grade, hw_grades in grades:

        sum_test_grades += test_grade
        sum_hw_grades += (sum(sorted(hw_grades[1:3])) / 2)

    
    # --- Plug the values to the formual and return ---
        
    
    w = (target_average * len(grades) - sum_hw_grades) / (sum_test_grades - sum_hw_grades)

    # There is a valid w.
    if w <= 1 and w >= 0:
        return w

    # Such a shame, the target average is not reachable.
    return None
    

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

def my_test():
    """
        More strict tests.
    """

    # --- Question 1 ---
    
    # 1 a
    if divisors(6) != [1, 2, 3]:
        print("divisors error 1")
    if divisors(0) != []:
        print("divisors error 2")

    # 1 b
    if perfect_numbers(1) != [6]:
        print("perfect_numbers error 1")
    if perfect_numbers(2) != [6, 28]:
        print("perfect_numbers error 1")

    # 1 c
    if abundant_density(20) != 0.15:
        print("abundant_density error 1")

    # 1 e
    if not semi_perfect_4(20):
        print("semi_perfect_4 error 1")
    if semi_perfect_4(28):
        print("semi_perfect_4 error 2")

    # --- Question 2 ---

    # 2 a
    if coin() not in [True, False]:
        print("coin error 1")

    # 2 b
    if True in [roll_dice(5) not in list(range(1, 6)) for i in range(30)]:
        print("roll_dice error 1")

    # 2 c
    if True in [roulette(1000, "even") not in [0, 2000] for i in range(30)]:
        print("roullete_repeat error 1")
    if True in [roulette(30, "odd") not in [0, 60] for i in range(30)]:
        print("roullete_repeat error 2")

    # 2 d
    awards_spectrum = list(range(-2500*10, 2500*10, 2500))
    if True in [roulette_repeat(2500, 10) not in awards_spectrum for i in range(30)]:
        print("roullete_repeat error 1")
    awards_spectrum = list(range(-30*500, 30*500, 30))
    if True in [roulette_repeat(30, 500) not in awards_spectrum for i in range(30)]:
        print("roullete_repeat error 2")

    # 2 e
    if True in [element not in ["a", 5, "!dd", 0.1, "&&&"] for element in shuffle_list(["a", 5, "!dd", 0.1, "&&&"])]:
        print("shuffle_list error 1")

    # ----- Question 3 -----

    # 3 a
    if inc("1000") != "1001":
        print("inc error 1")
    if inc("1001") != "1010":
        print("inc error 2")
    if inc("1011") != "1100":
        print("inc error 3")
    if inc("1111111111") != "10000000000":
        print("inc error 4")
    if inc("11110") != "11111":
        print("inc error 5")

    # 3 b
    if add("1", "1") != "10":
        print("add error 1")
    if add("0", "0") != "0":
        print("add error 2")
    if add("100", "1") != "101":
        print("add error 3")
    if add("111", "1") != "1000":
        print("add error 4")
    if add("11", "110") != "1001":
        print("add error 5")

    # 3 c

    # 3 d

    # 3 e
    if not leq("0", "1"):
        print("leq error 1")
    if not leq("1", "1"):
        print("leq error 2")
    if leq("1", "0"):
        print("leq error 3")
    if not leq("1", "10"):
        print("leq error 4")
    if leq("10", "1"):
        print("leq error 5")
    if not leq("1111111011", "1111111101"):
        print("leq error 1")

    # 3 f
    if not to_decimal("10") == 2:
        print("to_decimal error 1")
    if not to_decimal("1") == 1:
        print("to_decimal error 2")
    if not to_decimal("0") == 0:
        print("to_decimal error 3")
    if not to_decimal("110") == 6:
        print("to_decimal error 4")
    if not to_decimal("1000") == 8:
        print("to_decimal error 5")
    if not to_decimal("1010") == 10:
        print("to_decimal error 6")

    # ----- Question 4 -----

    # 4 a
    if lychrel_loops(28) != 2:
        print("lychrel_loops error 1")
    if lychrel_loops(110) != 1:
        print("lychrel_loops error 2")
    if lychrel_loops(19) != 2:
        print("lychrel_loops error 3")

    # 4 b
    if not is_lychrel_suspect(28, 1):
        print("is_lychrel_suspect error 1")
    if is_lychrel_suspect(28, 2):
        print("is_lychrel_suspect error 1")

    # 4 c
    if lychrel_sort([165, 164, 196, 28, 110], 8) != [110, 28, 165, 164, 196]:
        print("lychrel_sort error 1")
    if lychrel_sort([165, 1947, 164, 196, 28, 1587, 110], 8) != [110, 28, 165, 164, 1947, 196, 1587]:
        print("lychrel_sort error 2")
    if lychrel_sort([165, 1947, 164, 19, 196, 28, 1587, 110], 8) != [110, 19, 28, 165, 164, 1947, 196, 1587]:
        print("lychrel_sort error 3")
    if lychrel_sort([165, 1947, 164, 28, 196, 19, 1587, 110], 8) != [110, 28, 19, 165, 164, 1947, 196, 1587]:
        print("lychrel_sort error 4")

    # ----- Question 5 -----

    # 5 c ii
    grades = [(90, (85, 90, 90)), (92, (85, 90, 90))]
    target_average = 95
    if calculate_w(grades, target_average):
        print("calculate_w error 1")

    grades = [(90, (85, 90, 90)), (92, (85, 90, 90))]
    target_average = 70
    if calculate_w(grades, target_average):
        print("calculate_w error 2")

    grades = [(93, (85, 90, 90)), (93, (85, 90, 90))]
    target_average = 90
    if calculate_w(grades, target_average) != 0:
        print("calculate_w error 3")

    grades = [(93, (85, 90, 90)), (93, (85, 90, 90))]
    target_average = 91
    if calculate_w(grades, target_average) - 0.33333 > 0.0001:
        print("calculate_w error 4")

    grades = [(85, (85, 90, 90)), (85, (85, 90, 90)), (85, (85, 90, 90)), (85, (85, 90, 90))]
    target_average = 86
    if calculate_w(grades, target_average) - 0.8 > 0.0001:
        print("calculate_w error 5")


print("runnign tests..")
my_test()
test()
print("all tests completed.")
