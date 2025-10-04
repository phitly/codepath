'''#A pangram is a sentence that contains every letter of the English alphabet at least once, regardless of case. Write a function to determine if a given sentence is a pangram.



## Understanding the Problem
### Questions
#1. Should the function consider only alphabetic characters and ignore numbers, punctuation, and spaces?
#   - Yes, only alphabetic characters should be considered.
#2. null? empty string?
#   - An empty string should return False as it does not contain any letters.


### Test Cases
#1. Input: "The quick brown fox jumps over the lazy dog"
#   Output: True
#2. Input: "Hello, World!"
#   Output: False
#3. Input: "A quick movement of the enemy will jeopardize five gunboats"
#   Output: True
#4. Input: ""
#   Output: False
#5. Input: "abcdefghijklmnopqrstuvwxyz"
#   Output: True
#6. Input: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#   Output: True
#7. Input: "The quick brown fox jumps over the lazy dog 123!"
#   Output: True


eng_alphabet=26
### Implementation
def is_pangram(sentence):
    #if string is empty
    if not sentence:
        return False
    #declare an empty set to hold the letters in the sentence
    sentence_letters = set()
    for char in sentence:
        #check if the character is a letter
        if char.isalpha():
            sentence_letters.add(char.lower())  # Convert to lowercase for case-insensitive comparison
    #check if the length of the set is 26 (number of letters in the alphabet)
    return len(sentence_letters) == 26


  #example usage - testing all cases
print("Test 1:", is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print("Test 2:", is_pangram("Hello, World!"))  # False
print("Test 3:", is_pangram("A quick movement of the enemy will jeopardize five gunboats"))  # True
print("Test 4:", is_pangram(""))  # False
print("Test 5:", is_pangram("abcdefghijklmnopqrstuvwxyz"))  # True
print("Test 6:", is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # True
print("Test 7:", is_pangram("The quick brown fox jumps over the lazy dog 123!"))  # True

'''

'''
Problem 1: Calling Mississippi

Copy and paste the following function:

def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")

Call the function so that it prints out the following to the console (without calling the function more than once):

1 mississipi
2 mississipi
3 mississipi
4 mississipi
5 mississipi

✨ AI Hint: String Interpolation
'''
'''
def count_mississippi(limit):
    for num in range(1, limit+1):
        print( f"{num} mississippi")
count_mississippi(5)
'''
#Problem 2: Swap Ends

## understanding the Problem
### Questions
#1. the len of string has to be greater than 1
#2. what if the string is empty?
#   - if the string is empty, return the empty string
#3. what if the string has only one character?
#   - if the string has only one character, return the string as is 
### Test Cases
#1. Input: "hello"
#   Output: "oellh"
#2. Input: "a"
#   Output: "a"
#3. Input: ""
#   Output: """"
#4. Input: "ab"
#   Output: "ba"
#5. Input: "abc"
#   Output: "cba"

### Implementation
#pseudo
'''
func of swap_ends (my_str) 
    check if len string is <=1 
        if so return the my_str
    return my_str[-1] + my_str[1:-1] + my_str[0]
###Write a function swap_ends() that accepts a string my_str as a parameter and returns a new string where the first and last characters from my_str are swapped.
'''
def swap_ends(my_str):
    if len(my_str) <= 1:
        return my_str
    return my_str[-1] + my_str[1:-1] + my_str[0]
    pass

#Example Usage:

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)


'''
#Problem 4: Reverse String

#Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.
'''

## Understand
# ask 
    # what if the input is empty
    # what if the string is a single char strin? 
#edge case
    #my_str([])=[]
    #my_stre([l])=l
    
#plan
    # pseudo
    # funtion reverser string (my_str)
    # return my_str from end to start in steps of -1
    # : : -1 
    # so what is : ? so depends on -1 or 1 it will go from start to end or end to start 
def reverse_string(my_str):
    return my_str[::-1]
#Example Usage:

my_str = "live"
print(reverse_string(my_str))

#Example Output: evil




'''

###Problem 5: First Unique

###Write a function first_unique_char() that given a string my_str as a parameter, it finds the first non-repeating character in it and returns its index. If it does not exist, then return -1.
'''
### Understand
# what is the question asking? 
# answer: to find the first non-repeating character in a string and return its index

# break down the problem
# 1. create a dictionary to store the count of each character in the string
    # meaning if we see a char we add it to the dict and set its count to 1
    # if we see the char again we increment its count by 1
# 2. iterate through the string and check the count of each character in the dictionary
    # if the count is 1 we return the index of that character
    # if we finish iterating through the string and do not find any character with count 1 we return -1
### Implementation


def first_unique_char(my_str):
    count = {}
    for char in my_str:
        # count.get(char,0) returns the count of char if it exists in the dic else it returns 0
        # the method is count.get(key, default)
        count[char] = count.get(char, 0) + 1
    # iterate through the string again to find the first unique character
    # we use enumerate to get the index and the character
    # enumerate returns a tuple of (index, character)
    #
    for i, char in enumerate(my_str):
        if count[char] == 1: # if the count of the character is 1 we return its index
            return i
    return -1 # if we do not find any unique character we return -1

#Example Usage:

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))

#Example Output

#0
#2
#-1

'''
#Problem 6: Minimum Distance

#Write a function min_distance() that takes in a list of strings words and two strings word1 and word2' as parameters. The function should return the minimum distance between word1 and word2 in the list of words. The distance between one word and an adjacent word in the list is 1.

def min_distance(words, word1, word2):
    pass

#Example Usage:

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)

#Example Output:

3
1
2


#PsuedoCode
# def min_distance(words, word1, word2):
# Check if word1 and word2 are in the list - 0
#word list <=1, Return 0
#Var1 - = -1, 
#var2 
'''