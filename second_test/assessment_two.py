class AssessmentTwo:

    # ===== BASIC =====

    def count_negative_numbers(self, numbers):
        """Return the number of negative values in the list."""
        count = [x for x in numbers if x < 0]
        return len(count)

    def average(self, numbers):
        """Return the average of numbers or None if list is empty."""
        total = 0
        if numbers:
            for number in numbers:
                total += number
        else:
            return None

        return total / len(numbers)

    def first_and_last(self, items):
        """Return a tuple of (first, last) item or None if list is empty."""
        if items:
            return (items[0], items[-1])
        else:
            return None

    def count_consonants(self, text):
        """Return the number of consonants in the string (letters only)."""
        vowels = "aeiou"
        cons = [ch.lower() for ch in text if ch.isalpha() and ch.lower() not in vowels]
        return len(cons)

    def is_even_length(self, text):
        """Return True if the string length is even."""
        if text:
            if len(text) % 2 == 0:
                return True
            else:
                return False
        else:
            return True


    # ===== INTERMEDIATE =====

    def remove_duplicates_preserve_order(self, numbers):
        """Remove duplicates while preserving order."""
        return list(set(numbers))

    def word_lengths(self, sentence):
        """Return a dictionary mapping each word to its length."""
        if sentence:
            pass
        else:
            return {}
        words = {}
        sentence_list = sentence.split(" ")

        for word in sentence_list:
            words.update({word: len(word)})

        return words

    def second_largest(self, numbers):
        """Return the second largest number or None if it doesn't exist."""
        if len(numbers) < 2:
            return None
        else:
            numbers.sort()
            return numbers[-2]

    def chunk_list(self, numbers, size):
        """Split list into chunks of given size."""
        if size <= 0:
            return None

        return [numbers[i : i + size] for i in range(0, len(numbers), size)]

    def is_anagram(self, s1, s2):
        """Return True if the two strings are anagrams (ignore case & spaces)."""
        # Remove spaces and lowercase
        s1_clean = s1.replace(" ", "").lower()
        s2_clean = s2.replace(" ", "").lower()

        # Count letters and compare
        return sorted(s1_clean) == sorted(s2_clean)

    # ===== ADVANCED =====

    def running_sum(self, numbers):
        """Return a list of running sums."""
        total = 0
        result = []

        for n in numbers:
            total += n
            result.append(total)

        return result

    def longest_unique_substring(self, text):
        """Return the length of the longest substring without repeating characters."""
        subs = []
        if text:
            for x in range(len(text)):
                current = []
                for char in text[x:]:
                    if char not in current:
                        current.append(char)
                subs.append(len(current))
        else:
            return 0
        
        return max(subs)

    def rotate_matrix_90(self, matrix):
        """Rotate a square matrix 90 degrees clockwise."""
        n = len(matrix)

        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse each row
        for row in matrix:
            row.reverse()

        return matrix

    def validate_palindrome_number(self, n):
        """Return True if integer n is a palindrome."""
        if n < 0:
            return False

        s = str(n)
        return s == s[::-1]

    def generate_pascal_row(self, n):
        """Return the nth row of Pascal's Triangle (0-indexed)."""
        row = [1]
        for _ in range(n):
            row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
        return row
