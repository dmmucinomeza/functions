'''
@author: Desteny Mucino Meza
'''

'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by 
calling the function and printing what is returned
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.
def subraction(num1,num2):
    differenceOfTwo = num2 - num1
    return differenceOfTwo

#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def quotient(num1):
    crazyFunction = ((num1/2)*77)+10000
    return crazyFuntion
#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def equality(num1, num2):
    b= num1 == num2
    return b 
#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def greater(num1, num2):
    greater_than = b>a
    return b 
#5) Define a function that takes in two words and returns a string that contains both words combined.
def two_words(word1, word2):
    combine_the_words= word1 + word2
    return combine_the_words
#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def compare_three_numbers(num1,num2,num3):
    result= (num1==num2) or (num1==num3)
    return result
#7) Define a function that prints your name.
def name(Desteny):
    result= Desteny
    return result
print(Desteny)
#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."
def compare_colors(fav, color):
    if color== fav :
        print("That's my favorite color")
    else:
        print("Thats not my favorite color, try again")
#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.
def compare_two_numbers(num1,num2):
    num1=4
    while num1 > 0:
        print(num1)
        num1 -=1
'''YOUR OWN FUNCTION'''
    

#10) Create your own function that solves any problem you can think of.
def destination(Desteny, Destination):
    if Desteny==Destination:
        print("That is my nickname")
    else:
        print("That is not my nickname, you are a snake.")