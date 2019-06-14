"""
Code Challenge
  Name: 
    Anagram
  Filename: 
    anagram.py
  Problem Statement:
   Two words are anagrams if you can rearrange the letters of one to spell the second.  
   For example, the following words are anagrams:
   ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']
   
  Create a function which takes two arguments and return whether they are angram or no ( True or False)
  
  Hint: 
   How can you tell quickly if two words are anagrams?  
   Dictionaries allow you to find a key quickly.  

"""


# Function to check the given words are anagram or not
def anagram_filter(word_1, word_2):
    if len(word_1) == len(word_2):
        if sorted(word_1) == sorted(word_2):
            return True
        else:
            return False
    else:
        return False
        

# Taking the words as input that are needed to be checked
first_word = input("Enter your first word here:")
second_word = input("Enter your second word here:")

# Final conclusion returned by function
final_result = anagram_filter(first_word, second_word)

if final_result == True :
    print ("Its Anagram")
else:
    print ("Not Anagram")