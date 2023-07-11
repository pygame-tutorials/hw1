"""
Section 2: Concept Questions [19 marks]

2.1 Write a function that takes in an input and checks to see 
if it’s an isogram. The function should return True or False. 

An isogram is a word where no letter is repeated.
Examples include:
"isogram"
"uncopyrightable"
“ambidextrously”

[7 marks]
 """
def isogram(word):
    word = word.lower() # convert word into lower case
  
    uniqueChars = set() # create empty set to store unique characters 
    
    # Using FOR loop iterate through each character in the word
    for character in word:
        if character in uniqueChars:  # Check if the character is already in the set stored
            return False # not true 

        uniqueChars.add(character) # add characters to the set 
    # If the characters are not in the set then they are unique therefore true 
    return True
word = input("Enter a word of your choice: ") # takes input of the chosen word
result = isogram(word) # calls isogram subroutine on word
print(result) # dispplays result 

"""
 2.2   Make a new test file and write comprehensive unit tests for the
             function you wrote in 2.1
             For each test case add a comment stating why you chose that case.

[12 marks]

"""


import unittest

class IsogramTestCase(unittest.TestCase):
    def test_empty_string(self):
        result = isogram("")
        self.assertTrue(result)
        # Theoretically speaking an empty string is an isogram because there are no repearing characters

    def test_isogram_name(self):
        result = isogram("Rosie")
        self.assertTrue(result)
        # The name 'Rosie' has no repeating characters therefore it shoild be considered an isogram

    def test_non_isogram_name(self):
        result = isogram("Samantha")
        self.assertFalse(result)
        # The name 'Samantha' has three repeating 'a' characters therefore it should not be considered an isogram

    def test_lower_case_word(self):
        result = isogram("ToMwAiTs")
        self.assertFalse(result)
        # The isogram function created earlier should treat the characters in a non-case sensitive manner and there are two repeats of 'T' therefore it should not be considered an isogram

  
    def test_word_with_space(self):
        result = isogram("hi there")
        self.assertFalse(result)
        # The function should only consider alphabetic characters therefore the space should be ignored and the word 'there' has a repeating 'e' twice therefore it should not be considered an isogram

    def test_special_chars(self):
        result = isogram("rosie@gmail.com")
        self.assertFalse(result)
        # The function should only consider alphabetic characters therefore the '@' symbol should be disregarded and the email comprises of reapeating characters of 'o', 'i' and 'm' therefore it should not be considered an isogram
if __name__ == '__main__':
    unittest.main()



