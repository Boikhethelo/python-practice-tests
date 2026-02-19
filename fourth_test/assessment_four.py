# =========================
# Assessment 4
# =========================


# ========= BASIC =========

def count_unique_elements(items):
    """Return the number of unique elements in the list."""
    return len(set(items))


def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries, overriding values from the first with the second."""
    pass


def format_student_report(name, marks):
    """Return a formatted report showing a student's name and average mark."""
    total = 0
    for mark in marks:
        total += mark
    
    return f"{name} averaged {total/len(marks)}"


def compress_string(text):
    """Compress a string by counting consecutive characters."""
    # output = ""
    # list_text = list(text)
    # for char in list_text:
    #     if char not in output:
    #         output = output + f"{char} {list_text.count(char)}"
    #     else:
    #         pass
    
    # return output

    if not text:
        return ""

    output = ""
    count = 1
    prev_char = text[0]

    for char in text[1:]:
        if char == prev_char:
            count += 1
        else:
            output += f"{prev_char}{count}"
            prev_char = char
            count = 1

    # Add the last run
    output += f"{prev_char}{count}"

    return output


# ======= INTERMEDIATE =======

def group_by_length(words):
    """Group words into a dictionary based on their length."""
    pass


def reverse_list_recursively(items):
    """Reverse a list using recursion."""
    pass


def rotate_matrix_90(matrix):
    """Rotate a square matrix 90 degrees clockwise."""
    pass


# ========= ADVANCED =========

def flatten_nested_list(nested):
    """Flatten a nested list of arbitrary depth using recursion."""
    pass


def sum_nested_numbers(nested):
    """Return the sum of all numbers in a nested list using recursion."""
    pass


def generate_pascal_row(n):
    """Return the nth row of Pascal's Triangle using recursion."""
    pass
