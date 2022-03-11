#Skeleton file for HW1 - Spring 2022 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.
#you can add new functions if needed.

#Change the name of the file to include your ID number (hw1_ID.py).

#Question 4a
def replace(text, alphabet, new_alphabet):
    pass

#Question 4b
def is_pal(text):
    pass

#Question 4c
def num_different_letters(text):
    chars = "abcdefghijklmnopqrstuvwxyz"
    pass

#Question 4d
def most_frequent(text):
    pass

#Question 4e
def kth_order(text, k):
    pass

#Question 5
def calc(expression):
    pass

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




