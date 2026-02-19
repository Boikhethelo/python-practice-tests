class AssessmentThree:

    # ===== BASIC =====

    def count_truthy(self, items):
        """Return how many values in the list evaluate to True."""
        output = [x for x in items if x == True]
        return len(output)

    def clamp(self, value, minimum, maximum):
        """Clamp value so it stays within [minimum, maximum]."""
        return max( minimum , min(value, maximum))

    def remove_whitespace(self, text):
        """Return the string with all whitespace removed."""
        #output = [x for x in text if x.isalnum()] 
        output = [x for x in text if not x.isspace()]
        return "".join(output)

    def all_unique(self, items):
        """Return True if all items in the list are unique."""
        output = set(items)
        if output == items:
            return True
        else:
            return False

    def title_case(self, sentence):
        """Capitalize the first letter of each word."""
        sentence_list = sentence.split(" ")
        output = [word.capitalize() for word in sentence_list]

        return " ".join(output)


    # ===== INTERMEDIATE =====

    def frequency_sort(self, numbers):
        """
        Return a list sorted by frequency (ascending),
        then by value (ascending).
        """
        output = sorted(numbers , key=numbers.count , reverse=False)

        return output

    def merge_intervals(self, intervals): #NB
        """
        Merge overlapping intervals.
        Example: [[1,3],[2,6],[8,10]] -> [[1,6],[8,10]]
        """
        if not intervals:
            return []
        
        intervals.sort(key = lambda x: x[0])
        merged = [intervals[0]]
        for current in intervals[1:]:
            last = merged[-1]

            if current[0] <= last[1]:
                last[1] = max(last[1] , current[1])
            else:
                merged.append(current)
        
        return merged
        


    def longest_word_length(self, sentence):
        """Return the length of the longest word."""
        if not sentence:
            return 0
        
        words = sentence.split()
        count = [len(x) for x in words]

        return max(count)
        # return max((len(word) for word in sentence.split()) , default=0)

    def prefix_sums(self, numbers):
        """Return a list of prefix sums."""
        output = []
        total = 0

        for num in numbers:
            total += num
            output.append(total)
        
        return output


    def valid_binary_string(self, s):
        """Return True if string contains only 0s and 1s."""
        if not s:
            return False
        
        binary_list = list(s)
        for x in binary_list:
            if x != "1" and x != "0":
                return False
        
        return True


    # ===== ADVANCED =====

    def product_except_self(self, numbers): #NB
        """
        Return an array where each element is the product of all
        other elements except itself.
        """
        output = []

        for i in range(len(numbers)):
            total = 1
            for j in range(len(numbers)):
                if i != j:
                    total *= numbers[j]
            output.append(total)

        return output


    def spiral_order(self, matrix):
        """
        Return all elements of the matrix in spiral order.
        """
      
        if not matrix:
            return []
        else:
            l = len(matrix[0])
            output = []
        
        order = True

        for numbers in matrix:
                if order == True:
                    output.append(numbers)
                else:
                    output.append(numbers[::l-1])
        order = not order
        
        return output




    def longest_palindromic_substring(self, s):
        """Return the longest palindromic substring."""
        pass

    def count_islands(self, grid):
        """
        Count the number of islands (1s connected horizontally or vertically).
        """
        pass

    def validate_sudoku(self, board):
        """
        Validate a partially-filled 9x9 Sudoku board.
        """
        pass
