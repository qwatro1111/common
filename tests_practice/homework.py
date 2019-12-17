def task_1(a, b):
    """
    Take two lists, say for example these two:
    a =[1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b =[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
    """
    return list(set(a).intersection(b))


def task_2(my_string):
    """
    Return the number of times that the letter “a” appears anywhere in the given string
    Given string is “I am a good developer. I am also a writer” and output should be 5.
    """
    return my_string.count('a')


def task_3(x):
    """
    Write a Python program to check if a given positive integer is a power of three
    Input : 9
    Output : True
    """
    n = 27
    p = x
    while p <= n:
        if p == n:
            return True
        else:
            p = p * x
    return False


def task_4(num):
    """
    Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
    Input : 48
    Output : 3
    For example given number is 59, the result will be 5.
    Step 1: 5 + 9 = 14
    Step 1: 1 + 4 = 5:
    """
    while num > 10:
        num = sum([int(i) for i in str(num)])
    return num


def task_5(lst):
    """
    Write a Python program to push all zeros to the end of a list.
    Input : [0,2,3,4,6,7,10]
    Output : [2, 3, 4, 6, 7, 10, 0]
    """
    for i in lst:
        if i == 0:
            lst.append(lst.pop(lst.index(i)))
    return lst


def task_6(lst):
    """
    Write a Python program to check a sequence of numbers is an arithmetic progression or not.
    Input : [5, 7, 9, 11]
    Output : True
    In mathematics, an arithmetic progression or arithmetic sequence is a sequence of numbers such that the difference between the consecutive terms is constant.
    For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression with common difference of 2.
    """
    if len(lst) < 2:
        return False
    regularity = lst[1] - lst[0]
    for i in range(len(lst)):
        if i != 0 and lst[i] - lst[i - 1] != regularity:
            return False
    return True


def task_7(lst):
    """
    Write a Python program to find the number in a list that doesn't occur twice.
    Input : [5, 3, 4, 3, 4]
    Output : 5
    """
    return [i for i in lst if lst.count(i) == 1][0]


def task_8(lst):
    """
    Write a Python program to find a missing number from a list.
    Input : [1,2,3,4,6,7,8]
    Output : 5
    """
    lst = list(set([i for i in range(min(lst), max(lst))]) - set(lst))
    return lst[0]


def task_9(lst):
    """
    Write a Python program to count the elements in a list until an element is a tuple.
    Sample Test Cases:
    Input: [1,2,3,(1,2),3]
    Output: 3
    """
    count = 0
    for i in lst:
        if isinstance(i, tuple):
            break
        count += 1
    return count


def task_10(string):
    """
    Write a program that will take the str parameter being passed and return the string in
    reversed order. For example: if the input string is "Hello World and Coders" then your
    program should return the string sredoC dna dlroW olleH.
    """
    return string[::-1]


def task_11(num):
    """
    Write a program that will take the num parameter being passed and return
    the number of hours and minutes the parameter converts to (ie. if num = 63 then
    the output should be 1:3). Separate the number of hours and minutes with a colon.
    """
    hours = 0
    while num > 60:
        hours += 1
        num -= 60
    minutes = num
    return f'{hours}:{minutes}'


def task_12(string):
    """
    Write a program that will take the parameter being passed and return the largest
    word in the string. If there are two or more words that are the same length,
    return the first word from the string with that length. Ignore punctuation.
    Sample Test Cases:
    Input:"fun&!! time"
    Output:time
    Input:"I love dogs"
    Output:love
    """
    import re
    return max(re.sub(r"[^a-zA-Z]+", " ", string).split(" "), key=len)


def task_13():
    """
    Write a program (using functions!) that asks the user for a long string containing
    multiple words. Print back to the user the same string, except with the words in backwards order.
    For example:
    Input: My name is Michele
    Outout: Michele is name My:
    """
    string = input("Input a long string: ")
    return " ".join(string.split(" ")[::-1])


def task_14():
    """
    Write a program that asks the user how many Fibonnaci numbers to generate and then
    generates them. Take this opportunity to think about how you can use functions.
    Make sure to ask the user to enter the number of numbers in the sequence to
    generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next
    number in the sequence is the sum of the previous two numbers in the sequence.
    The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
    """
    n = input("How many Fibonnaci numbers to generate? ")
    a, b = 0, 1
    numbers = []
    for i in range(int(n)):
        a, b = b, a + b
        numbers.append(str(a))
    return True


def task_15(lst):
    """
    Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and makes a new list that has only the even
    elements of this list in it.
    """
    return [i for i in lst if i % 2 == 0]


def task_16(num):
    """
    Write a program that will add up all the numbers from 1 to input number.
    For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10.
    """
    return sum(i for i in range(num + 1))


def task_17(num):
    """
    Write a program that will take the parameter being passed and return the factorial of it.
    For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
    """
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial


def task_18(string):
    """
    Write a program that will take the str parameter being passed and modify it using
    the following algorithm. Replace every letter in the string with the letter following
    it in the alphabet (ie. cbecomes d, zbecomes a). Then capitalize every vowel in
    this new string (a, e, i, o, u) and finally return this modified string.
    Input: abcd
    Output: bcdE
    """
    my_string = ""
    for i in string:
        if i == 'z':
            my_string += 'a'
            continue
        elif i == 'Z':
            my_string += 'A'
            continue
        my_string += chr(ord(i) + 1)
    return "".join([i.upper() if i in 'aeiou' else i for i in my_string])


def task_19(string):
    """
    Write a program that will take the str string parameter being passed and return
    the string with the letters in alphabetical order (ie. hello becomes ehllo).
    Assume numbers and punctuation symbols will not be included in the string.
    Input: edcba
    Output: abcde
    """
    return "".join(sorted(string))


def task_20(num1, num2):
    """
    Write a program that will take both parameters being passed and return the true if num2 is greater
    than num1, otherwise return the false. If the parameter values are equal to each other then
    return the string -1
    """
    if num1 < num2:
        return True
    elif num1 > num2:
        return False
    elif num1 == num2:
        return '-1'
    return False
