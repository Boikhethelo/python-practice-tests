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
    if not words:
        return {}
    else:
        output = {}
    
    for word in words:
        if len(word) not in output:
            x = [w for w in words if len(w) == len(word)]
            output.update({len(word): x})
    
    return output


def reverse_list_recursively(items): #NB
    """Reverse a list using recursion."""
    if len(items) <= 1:
        return items
    return reverse_list_recursively(items[1:]) + [items[0]]

def rotate_matrix_90(matrix):
    """Rotate a square matrix 90 degrees clockwise."""
    pass


# ========= ADVANCED =========

def flatten_nested_list(nested):
    """Flatten a nested list of arbitrary depth using recursion."""
    result = []
    
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)
    
    return result


def sum_nested_numbers(nested):
    """Return the sum of all numbers in a nested list using recursion."""
    total = 0
    
    for item in nested:
        if isinstance(item, list):
            total += sum_nested_numbers(item)
        else:
            total += item
    
    return total

def generate_pascal_row(n):
    """Return the nth row of Pascal's Triangle using recursion."""
    if n == 0:
        return [1]
    
    previous_row = generate_pascal_row(n - 1)
    new_row = [1]
    
    for i in range(1, len(previous_row)):
        new_row.append(previous_row[i - 1] + previous_row[i])
    
    new_row.append(1)
    return new_row