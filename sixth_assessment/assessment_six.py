# =========================
# BASIC SECTION
# =========================

def sum_list(numbers):
    """
    Return the sum of all numbers in a list.
    """
    return sum(numbers)


def count_even(numbers):
    """
    Return the count of even numbers in a list.
    """
    #return len([x for x in numbers if x % 2 == 0])
    return sum(1 for x in numbers if x % 2 == 0)


def capitalize_sentence(sentence):
    """
    Return the sentence with the first letter of each word capitalized.
    """
    if sentence:
        output = []
    else:
        return ""
    
    words = sentence.split()
    
    output = [word.capitalize() for word in words ]

    return " ".join(output)


def reverse_string(s):
    """
    Return the reversed string.
    """
    return s[::-1]


def max_in_list(numbers):
    """
    Return the maximum number in a list. Return None if the list is empty.
    """
    if numbers:
        return max(numbers)
    else:
        return None


# =========================
# INTERMEDIATE SECTION
# =========================

def factorial(n):
    """
    Return the factorial of a non-negative integer n.
    """
    if n < 0 :
        return ValueError
    elif n ==1 or n == 0:
        return 1
    else:
        return factorial * factorial(n-1)


def remove_duplicates(lst):#NB
    """
    Return a list with duplicates removed while preserving order.
    """
    seen = set(set)
    output = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            output.append(item)

    return output



def sum_of_squares(numbers):
    """
    Return the sum of squares of all numbers in a list.
    """
    pass


def sort_dict_by_values(d):
    """
    Return a list of tuples sorted by dictionary values.
    """
    


def print_multiplication_table(n):
    """
    Return a 2D list representing the multiplication table up to n.
    """
    pass


# =========================
# ADVANCED SECTION
# =========================

def rotate_list(lst, k):
    """
    Rotate the list to the right by k steps.
    """
    pass


def fibonacci_list(n):
    """
    Return a list of Fibonacci numbers up to index n.
    """
    pass


def flatten_list(lst):
    """
    Recursively flatten a nested list of integers.
    """
    pass


def is_palindrome(s):
    """
    Recursively determine whether a string is a palindrome.
    """
    pass


def count_inversions(lst):
    """
    Return the number of inversions in a list (pairs where a[i] > a[j] for i < j).
    """
    pass
