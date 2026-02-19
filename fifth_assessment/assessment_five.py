# =========================
# Assessment 5
# =========================


# ========= BASIC =========

def count_occurrences(items):
    """Return a dictionary counting how many times each element appears."""
    if items:
        output = {}
    else:
        return {}
    
    for item in items:
        if item not in output.keys():
            output.update({item:items.count(item)})
        else:
            pass
    
    return output


def remove_duplicates(items):
    """Return a list with duplicates removed while preserving order."""
    if items:
        return set(items)
    else:
        return []


def format_price_list(prices):
    """Return a formatted string showing prices with two decimal places."""
    output = []

    for price in prices:
        output.append(f"{price:2f}")
    
    return " ".join(output)


# ======= INTERMEDIATE =======

def split_by_type(items):
    """Separate integers and strings into two lists stored in a dictionary."""
    output = {"integers" : [] , "strings" : []}

    for item in items:
        if type(item) == int:
            output["integers"].append(item)
        elif type(item) == str:
            output["strings"].append(item)
        else:
            pass
    
    return output
    # return {"intergers": [x for x in items if isinstance(x, int)],
    #         "string" : [x for x in items if isinstance(x. str)]}



def recursive_max(numbers):
    """Return the maximum number in a list using recursion."""
    pass


def transpose_matrix(matrix):
    """Return the transpose of a 2D matrix."""
    pass


# ========= ADVANCED =========

def deep_count(nested):
    """Count how many non-list elements exist in a nested list using recursion."""
    pass


def recursive_string_reverse(text):
    """Reverse a string using recursion."""
    pass


def generate_pascal_triangle(n):
    """Generate Pascal’s Triangle up to n rows using recursion."""
    pass
