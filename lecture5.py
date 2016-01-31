# __author__= "Di"

# Problem 1
# Write an iterative function iterPower(base, exp) that calculates the exponential baseexp
# by simply using successive multiplication.
# For example, iterPower(base, exp) should compute baseexp by multiplying base times itself exp times.
# Write such a function below. This function should take in two values -
# base can be a float or an integer; exp will be an integer ≥ 0.
# It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result


# Problem 2
# Write a function recurPower(base, exp) which computes baseexp by recursively calling itself
# to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.
# This function should take in two values - base can be a float or an integer; exp will be an integer ≥0.
# It should return one numerical value.
# Your code must be recursive - use of the ** operator or looping constructs is not allowed.


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return base * exp + 1
    else:
        return base * recurPower(base, exp - 1)


# Problem 3
# The function recurPower(base, exp) from Problem 2 computed baseexp by decomposing the problem
# into one recursive case and one base case.
# Write a procedure recurPowerNew which recursively computes exponentials using this idea.


def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    if exp > 0 and (exp % 2 == 0):
        return base * recurPowerNew(base, exp - 1)

    if exp > 0 and (exp % 2 != 0):
        return base * recurPowerNew(base, exp - 1)


# Problem 4
# Write an iterative function, gcdIter(a, b), that implements this idea.
# One easy way to do this is to begin with a test value equal to the smaller of the two input arguments,
# and iteratively reduce this test value by 1 until you either reach a case where the test divides
# both a and b without remainder, or you reach 1.


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    n = min(a, b)
    while n > 0:
        if a % n == 0 and b % n == 0:
            return n
        else:
            n -= 1


# Problem 5
# A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors.
# Suppose that a and b are two positive integers:
# If b = 0, then the answer is a
# Otherwise, gcd(a, b) is the same as gcd(b, a % b)
# Write a function gcdRecur(a, b) that implements this idea recursively.
# This function takes in two positive integers and returns one integer.


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


# Problem 6
# Write an iterative function, lenIter, which computes the length of an input argument (a string),
# by counting up the number of characters in the string.


def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    s = aStr
    count = 0
    for letter in s:
        count += 1
    return count


# Problem 7
# For this problem, write a recursive function, lenRecur,
# which computes the length of an input argument (a string), by counting up the number of characters in the string.


def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    a = aStr

    if a == '':
        return 0
    else:
        return 1 + lenRecur(a[0:-1])


# Problem 8
# We can use the idea of bisection search to determine if a character is in a string,
# so long as the string is sorted in alphabetical order.
# First, test the middle character of a string against the character you're looking for (the "test character").
# If they are the same, we are done - we've found the character we're looking for!
# If they're not the same, check if the test character is "smaller" than the middle character.
# If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string.
# (Note that you can compare characters using Python's < function.)
# Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr.
# char will be a single character and aStr will be a string that is in alphabetical order. T
# he function should return a boolean value.
# As you design the function, think very carefully about what the base cases should be.


def isIn(letter, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    aStrsorted = sorted(aStr.lower())

    low = 0
    high = len(aStrsorted)
    middle = (low + high) / 2
    i = 0
    while i < 50:
        i += 1
        if len(aStr) <= 0:
            return False
        if letter == aStrsorted[middle]:
            return True
        if (low == middle or high == middle) and (letter != aStrsorted[middle]):
            return False
        else:
            if letter > aStrsorted[middle]:
                low = middle
                return isIn(letter, aStrsorted[low:high])
            else:
                high = middle
                return isIn(letter, aStrsorted[low:high])


# Problem 9
# A semordnilap is a word or a phrase that spells a different word when backwards
# ("semordnilap" is a semordnilap of "palindromes").
# Here are some examples:
# nametag / gateman
# dog / god
# live / evil
# desserts / stressed
# Write a recursive program, semordnilap, that takes in two words and says if they are semordnilap.
# This recursive function is not entirely straightforward. There are a few things that you need to
# check the first time you look at the inputs that you should not check on subsequent recursive calls:
# you need to make sure that the strings are not single characters,
# and also you need to be sure that the strings are not equal.
# If you do this check every time you call your function, though,
# this will end up interfering with the recursive base case (which we don't want!).
# There's a few different ways you can perform checks on the inputs the first time.
# The first way would be to use keyword arguments.
# The second way would be to use a global variable, which you'll see in the next lecture video; however,
# using global variables is always a bit risky and thus not the best way to do this.
# The third way to perform checks on the inputs the first time you see them,
# but not any subsequent time, is to use a wrapper function.
# This wrapper function performs some checks, then makes a call to the recursive function.


def semordnilap(str1, str2):
    if len(str1) != len(str2):
        return False

    if (len(str1) > 0) and (len(str2) > 0):
        if len(str1) == 1:
            return str1 == str2
        if str1[0] == str2[-1]:
            return semordnilap(str1[1:], str2[:-1])
        else:
            return False
