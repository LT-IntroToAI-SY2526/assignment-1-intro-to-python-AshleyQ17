# Assignment 1: AI-Generated Python Problems
# Name: [Ashley Quiroz]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

MY ORIGINAL AI PROMPT:
"I'm learning Python basics in a high school programming class. I have some experience from my AP CSP class. Can you create 6 practice problems that cover: 
> - Variables and basic data types
> - Conditionals (if/elif/else)
> - Loops (for and while)
> - Functions
> - Basic list operations
> 
> Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs."

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
#==============================================================================
"""
Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.
Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False

PROBLEM 1: [Warm-up: Favorite Number (Variables and Data types)]
[Write a program that asks the user for their name and their favorite number. Print a message that includes their name and the square of their favorite number.
"""
def square_favorite(name, fav_num):
    return "Hi {name}! The square of your favorite number is {fav_num ** 2}."

"""

Problem 2: [Even or Odd? Conditionals]
[Ask the user to enter an integer. Use an if/else statement to check if it is even or odd, then print the result]
"""
def is_even(num):
    return num % 2 == 0
"""
Problem 3: [Multiplication Table (Loops - for loops)]
[Write a program that asks for a number and prints its multiplication table up to 10. Use a for loop.]
"""
def multiplication_table(num):
    result = []
    for i in range(1, 11):
        result.append(f"{num} x {i} = {num * i}")
    return result
"""
# Example tests
print(multiplication_table(5))
# ['5 x 1 = 5', '5 x 2 = 10', ..., '5 x 10 = 50']


Problem 4: [Number Guessing Game (Loops - while loop + Conditionals)]
[Pick a secret number (e.g., 7). Ask the user to keep guessing until they get it right. Tell them if their guess is too high or too low.]
"""
secret = 7  # this number can be changed
guess = None

while guess != secret:
    guess = int(input("Guess the number: "))
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed it.")
"""
Problem 5: [Word Reverser (Functions + Strings)]
[Write a function reverse_word(word) that takes a word and returns it reversed. Ask the user for a word, call the function, and print the result.]
Example: 
"""
def reverse_word(word):
    return word[::-1]  # slicing trick

user_word = input("Enter a word: ")
print("Reversed:", reverse_word(user_word))
"""
Problem 6:[List Statistics (Lists + Functions)]
[Ask the user for 5 numbers and store them in a list. Write a function list_stats(numbers) that returns the minimum, maximum, and average of the list. Print the results.]
"""
def list_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""
"""Practice Problem 1"""
print(square_favorite("Alice", 7))
# Should print "Hi Alice! The square of your favorite number is 49."

"""Practice Problem 2"""
print(is_even(4))  # Should print "True"
print(is_even(7))  # Should print "False"

"""Practice Problem 3"""
print(multiplication_table(5)) # Should print ['5 x 1 = 5', '5 x 2 = 10', ..., '5 x 10 = 50']

"""Practice Problem 4"""
print(check_guess(7, 3))   # Should print "Too low!"
print(check_guess(7, 9))   # Should print "Too high!"
print(check_guess(7, 7))   # Should print "Correct!"

"""Practice Problem 5"""
print(reverse_word("hello"))  # Should print "olleh"
print(reverse_word("python")) # Should print "nohtyp"

"""Practice Problem 6"""
print(list_stats([3, 8, 2, 10, 6])) # Should print "(2, 10, 5.8)"
