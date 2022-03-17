from timeit import timeit


def max_even_seq(n):
    """
        The function receives a positive integer n >= 0.
        It calculates and returns the length of the maximum even digits sequence in the received number, n.
    """

    # Loop initiation.
    
    # The current sequence counter.
    current_counter = 0

    # The maximum sequence till the current iteration.
    max_counter = 0

    # Iterate over the digits of n.
    while n > 0:

        # The current most right digit is even.
        if n % 2 == 0:

            # Increase the current sequence by 1.
            current_counter += 1

        # The current most right digit is odd.
        else:

            # The current sequence is broken. Check if it is greater than the current maximum sequence.
            if current_counter > max_counter:

                # The max counter is now the current counter.
                max_counter = current_counter

            # Reset the current counter.
            current_counter = 0

        # Cut the right digit.
        n = n // 10

    # This check is relevant if the leftest digit of n is even.
    if current_counter > max_counter:

        # Update the max counter.
        max_counter = current_counter

    # Return the greatest sequence.
    return max_counter
                


########
# Tester
########


def test():
    if max_even_seq(23300247524689) != 4:
        print("error in max_even_seq")

print("123468579", "result:", max_even_seq(123468579), "exepted: 3")
print("2461285", "result:", max_even_seq(2461285), "exepted: 3")
print("1359", "result:", max_even_seq(1359), "exepted: 0")
print("2468", "result:", max_even_seq(2468), "exepted: 4")


print(timeit(lambda: max_even_seq(11111111111111111111), number=10000))
print(timeit(lambda: max_even_seq(22222222222222222222), number=10000))
print(timeit(lambda: max_even_seq(12121212121212121212), number=10000))
print(timeit(lambda: max_even_seq(99999999999999999999), number=10000))
