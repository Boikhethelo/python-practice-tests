class PracticeExam:

    # ===== BASIC QUESTIONS =====

    def count_odd_numbers(self, numbers):
        """Return the count of odd numbers in the list."""
        count = 0
        for num in numbers:
            if num % 2 > 0:
                count += 1
        
        return count

    def sum_list(self, numbers):
        """Return the sum of all numbers in the list."""
        total = 0

        for num in numbers:
            total += num
        
        return total

    def reverse_words_order(self, sentence):
        """Reverse the order of words in a sentence."""
        
        sentence_list = sentence.split(" ")
        reversed_words = []

        for i in range(len(sentence_list) -1, -1 , -1):
            reversed_words.append(sentence_list[i])
        
        return " ".join(reversed_words)
        
       
    

    def contains_vowel(self, text):
        """Return True if the string contains at least one vowel."""
        vowels = ['a' , 'i' , 'o' , 'u' , 'e']

        for letter in text:
            if letter.lower() in vowels:
                return True
            else:
                pass
        
        return False

    def smallest_number(self, numbers):
        """Return the smallest number in the list or None if empty."""
        
        if numbers: 
            numbers.sort()
            return numbers[0]
        else:
            return None


    # ===== INTERMEDIATE QUESTIONS =====

    def remove_vowels(self, text):
        """Return the string with all vowels removed (case-insensitive)."""
        vowels = ['a' , 'i' , 'o' , 'u' , 'e']
        new_string = []

        for letter in text:
            if letter.lower() in vowels:
                pass
            else:
                new_string.append(letter)
        
        return "".join(new_string)
            

    def count_character_frequency(self, text):
        """Return a dictionary with character frequencies."""
        new_dict = {}

        for letter in text:
            new_dict.update({letter:0})

            for i in range(len(text)):
                if text[i] ==letter:
                    new_dict[letter] += 1
                else:
                    pass
        return new_dict


    def is_prime(self, n):
        """Return True if n is a prime number, otherwise False."""

        if n <= 1:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True



    def flatten_list(self, nested):
        """Flatten a 2D list into a 1D list."""
        new_list = []
        for x in nested:
            for y in x:
                new_list.append(y)
        
        return new_list

    def longest_common_prefix(self, words):
        """Return the longest common prefix among a list of words."""

        if not words:
            return ""

        prefix = words[0]

        for word in words[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix




        
        



    # ===== ADVANCED QUESTIONS =====

    def fibonacci_sequence(self, n):
        """Return a list containing the first n Fibonacci numbers."""
        if n <= 0:
            return []

        if n == 1:
            return [0]

        fibs = [0, 1]

        while len(fibs) < n:
            fibs.append(fibs[-1] + fibs[-2])

        return fibs
    


    def max_subarray_sum(self, numbers):
        """Return the maximum sum of a contiguous subarray."""
        totals = []

        for i in range(len(numbers)):
            total = 0
            for num in numbers[i:]:
                total += num
                totals.append(total)

        return max(totals)


    def valid_parentheses(self, s):
        """Return True if parentheses are valid."""
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in pairs.values():          # opening bracket
                stack.append(ch)
            elif ch in pairs:                 # closing bracket
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return not stack

    def rotate_left(self, numbers, k):
        """Rotate the list to the left by k positions."""

        if not numbers:
            return numbers

        k %= len(numbers)
        return numbers[k:] + numbers[:k]


    def spiral_matrix(self, n):
        """Return an n x n spiral matrix."""

        if n <= 0:
            return []

        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1

        while top <= bottom and left <= right:
            # left → right
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            # top → bottom
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            # right → left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1

            # bottom → top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1

        return matrix


test = PracticeExam()

print(test.reverse_words_order('hello world python'))

