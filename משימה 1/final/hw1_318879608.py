#Question 4a
def replace(text, alphabet, new_alphabet):
    """
        The function receives a text string and alphabet, new alphabet strings which act as a dictionary.
        It replaces each character in the text which appears in the alphabet string with the corresponding
        character in the new_alphabet string.
        The function returns the modified text string.
        Note that alphabet has no characters repetition, and alphabet, new_alphabet strings share the same length.
        Text must contain only the following characters: 0-9, a-z, [space], '.'.
    """

    # If alphabet is empty, nothing should be changed in text, don't bother entering the loop.
    if not alphabet:
        return text
    
    # The string that will contain the modified text string.
    new_text = ""

    # Will contain in the following loop the correct new character that needs to be appended to new_text.
    new_char = ""
    
    # Iterate over the characters of the received text.
    for current_char in text:

        # Check if the alphabet string has the current character in it.
        if current_char in alphabet:

            # It has, find the corresponding character in the new alphabet string and save it as the new character.
            new_char = new_alphabet[alphabet.index(current_char)]

        # The current character is not in the alphabet string.
        else:

            # Simply keep the current character as the new character.
            new_char = current_char

        # Append the new character to the new_text string.
        new_text += new_char

    # Return the correct new text.
    return new_text

#Question 4b
def is_pal(text):
    """
        The function receives a text and returns True if the text string is an extended polyndrom.
        Otherwise returns False.
    """

    # First, remove the dots and spaces in the function.
    text = text.replace(" ", "").replace(".", "")

    # Iterate over the text till the middle, floored if odd.  
    for i in range(int(len(text)/2)):

        # The current character is not the same as its mirror.
        if not text[i] == text[-i - 1]:

            # Not a syndrom.
            return False

    # Indeed a syndrom, all the characters are mirrored as required.
    return True

#Question 4c
def num_different_letters(text):
    """
        The function recieves a text string and returns how many letters from the alphabet appears in the text.
    """

    # A string with all the alphabet letters.
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # A string for the following loop. Each character in the current string has already appered in a previous iteration.
    appeared = ""

    # Iterate over the characters of the received text string.
    for current_char in text:

        # Check if the current char is a letter from the alphabet and hasn't appeared in previous iterations.
        if current_char in alphabet and not current_char in appeared:

            # Note that the current char has appeared in the text.
            appeared += current_char

    # Return how many different letters appears in the received text.
    return len(appeared)

#Question 4d
def most_frequent(text):
    """
        The function returns the character with the most apearences in the received text string.
        Note: the text string cannot share more than one characters with the most appearences.
        - If text is the empty string, i.e "", the function returns ''.
    """

    # If text is the empty string, don't bother. Note: check was not required, but can help kth_order with empty string.
    if not text:
        return ''
    
    # A string with all the allowd characters.
    allowed_characters = "abcdefghijklmnopqrstuvwxyz0123456789. "

    # Create a dictionary of counters, with the allowed characters as keys.
    characters_counters = {char: 0 for char in allowed_characters}

    # The current maximum character counter.
    max_character_counter = "a"
    
    # Iterate over the characters of the received text.
    for current_char in text:

        # Increase the counter of the current character by 1.
        characters_counters[current_char] += 1

        # If the current character counter greater than the current maximum character counter.
        if characters_counters[current_char] > characters_counters[max_character_counter]:

            # Update the max character counter to point on the current character.
            max_character_counter = current_char

    # Return the character with the most appearences.
    return max_character_counter
        
#Question 4e
def kth_order(text, k):
    """
        The function receives a text string and a natural number, k.
        It returns the k'th most frequent number.
        Note that there must be k different characters in the text, and there are no characters with the same frequency.
        Side-note: It would obviously be more efficient to find the k'th most frequent character by simply checking the counters dictionary
                   in the most_frequent function above (only O(n) instead of O(n*k)).
        - If text is the empty string, i.e "", the function returns ''.
    """

    # Iterate k times.
    for i in range(k - 1):

        # Get the most frequent character in the current text string, and remove it from the text.
        text = text.replace(most_frequent(text), '')

    # Return the k'th frequent character.
    return most_frequent(text)
        

#Question 5
def calc(expression):
    """
        The function receives expression as a string and returns a string following the expression commands. 
    """

    # Received the empty string.
    if not expression:

        # Return the empty string.
        return ""
    
    # First, split the expresion to a list of string, command, string, command, ...., string.
    strings_commands = expression.split("'")[1:-1]

    # Create a list with the commands by order.
    commands = [strings_commands[i] for i in range(1, len(strings_commands), 2)]

    # Create a list with the strings by order.
    strings = [strings_commands[i] for i in range(0, len(strings_commands), 2)]
    
    # The following loop will construct the final string command by command. Assign the initial string to it.
    final_string = strings_commands[0]

    # Iterate on the strings and commands.
    for i in range(len(commands)):

        # Extract the current command and the current string.
        command = commands[i]
        string = strings[i + 1]

        # Switch case the current command.
        if command == "+":

            # Append the currrent string to the final string.
            final_string += string

        elif command == "-":

            # Remove all the instances of the current string (which is a char according to the expression requirements) from the current final string.
            final_string = final_string.replace(string, "")

        elif command == "*":

            # Regarding the expression requirements, string is an int which indicates on how many times the current final string needs to be duplicated.
            duplicate_times = int(string)

            # Duplicate the final string as required.
            final_string *= duplicate_times

    # Return the final string.
    return final_string

########
# Tester
########


def test():
    
    #testing Q4
    if replace("hello world", "abcde fghijkl", "1234567890xyz") != "95zzo6worz4":
        print("error in replace - 1")
    if replace("abcd123", "1", "x") != "abcdx23":
        print("error in replace - 2")
    
    if not is_pal("go dog"):
        print("error in is_pal - 1")
    if is_pal("anda"):
        print("error in is_pal - 2")
    
    if num_different_letters("aa bb cccc dd ee fghijklmnopqrstuvwxyz") != 26:
        print("error in num_different_letters - 1")
    if num_different_letters("aaa98765432100000000") != 1:
        print("error in num_different_letters - 2")
    
    if most_frequent("abcdee") != "e":
        print("error in most_frequent - 1")
    if most_frequent("x11x22x33x") != "x":
        print("error in most_frequent - 2")
    
    if kth_order("aaaabbbccd", 3) != "c":
        print("error in kth_order - 1")
    if kth_order("abcdabcaba", 1) != "a":
        print("error in kth_order - 2")

    #testing Q5
    if calc("'123321'*'2'") != "123321123321":
        print("error in calc - 1")
    if calc("'Hi there '*'3'+'you2'") != "Hi there Hi there Hi there you2":
        print("error in calc - 2")
    if calc("'hi+fi'*'2'*'2'") != "hi+fihi+fihi+fihi+fi":
        print("error in calc - 3")
    if calc("'a'*'2'+'b'*'2'") != "aabaab":
        print("error in calc - 4")
    if calc("'a'*'2'+'b'*'2'-'b'") != "aaaa":
        print("error in calc - 5")
    if calc("'a'*'2'+'b'*'2'-'c'") != "aabaab":
        print("error in calc - 6")


def my_test():

    # Testing Q4.

    # Make sure all the function handle text as an empty string correctly.
    if [replace("", "d", "d"), is_pal(""), num_different_letters(""), most_frequent(""), kth_order("", 0)] != ["", True, 0, '', '']:
        print("error empty string")

    # Check replace.
    if replace("", "gtd", "ooi") != "":
        print("error 1 in replace")
    if replace("hello there", "", "") != "hello there":
        print("error 2 in replace")
    if replace("09 . 5 d   g ... f", "", "") != "09 . 5 d   g ... f":
        print("error 3 in replace")
    if replace("09 . 5 d   g ... f", "9g", "1q") != "01 . 5 d   q ... f":
        print("error 3 in replace")
    if replace("  . .. ...", ". ", ",$") != "$$,$,,$,,,":
        print("error 4 in replace")
    if replace("04r. ", "$^.0", "dva3") != "34ra ":
        print("error 5 in replace")

    # Check is_pal.
    if is_pal("ada") is not True:
        print("error 1 in is_pal")
    if is_pal("adc") is not False:
        print("error 2 in is_pal")
    if is_pal("  ..  . .....    ..") is not True:
        print("error 3 in is_pal")
    if is_pal("  ..  . ...6..    ..") is not True:
        print("error 4 in is_pal")
    if is_pal("  ..  . .65....    ..") is not False:
        print("error 5 in is_pal")
    if is_pal("  ..  . .65....   6 ..") is not True:
        print("error 6 in is_pal")
    if is_pal("a656") is not False:
        print("error 6 in is_pal")

    # Check num_different_letters.
    if num_different_letters("") != 0:
        print("error 1 in num_different_letters")
    if num_different_letters("a") != 1:
        print("error 2 in num_different_letters")
    if num_different_letters("aa") != 1:
        print("error 3 in num_different_letters")
    if num_different_letters("ada") != 2:
        print("error 4 in num_different_letters")
    if num_different_letters("addaa") != 2:
        print("error 5 in num_different_letters")
    if num_different_letters("a.a") != 1:
        print("error 6 in num_different_letters")
    if num_different_letters("a a") != 1:
        print("error 7 in num_different_letters")
    if num_different_letters("a0") != 1:
        print("error 8 in num_different_letters")

    # Check most_frequent.
    if most_frequent("") != "":
        print("error 1 in most_frequent")
    if most_frequent("a") != "a":
        print("error 2 in most_frequent")
    if most_frequent("ada") != "a":
        print("error 3 in most_frequent")
    if most_frequent("d     . . d") != " ":
        print("error 4 in most_frequent")
    if most_frequent("t  ad dd.... qqq qqq qqqq qqqq") != "q":
        print("error 5 in most_frequent")
    if most_frequent("......... 0 ....") != ".":
        print("error 6 in most_frequent")
    if most_frequent("000000aa9") != "0":
        print("error 7 in most_frequent")

    # Check kth_order.
    if kth_order("", 3) != "":
        print("error 1 in kth_order")
    if kth_order("ab", 3) != "":
        print("error 2 in kth_order")
    if kth_order("ababc", 3) != "c":
        print("error 3 in kth_order")
    if kth_order("0    91444..", 3) != ".":
        print("error 4 in kth_order")
    if kth_order("         t9", 1) != " ":
        print("error 5 in kth_order")
    if kth_order("abcd eabcde", 6) != " ":
        print("error 6 in kth_order")
    if kth_order("  ..7", 3) != "7":
        print("error 7 in kth_order")

    # Testing Q5.
    if calc("") != "":
        print("error 1 in calc")
    if calc("'.'*'12'") != "............":
        print("error 2 in calc")
    if calc("''+'123'*'1'+''") != "123":
        print("error 3 in calc")
    if calc("''*9") != "":
        print("error 4 in calc")
    if calc("'a'-'a'-'t'") != "":
        print("error 5 in calc")
