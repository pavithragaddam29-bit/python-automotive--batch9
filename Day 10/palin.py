class PalindromicSubsequenceCounter:
    def __init__(self, s):
        self.s = s
        self.n = len(s)

    def validate_input(self):
        if self.n <= 1 or self.n >= 10:
            raise ValueError("String length must be between 2 and 9")

    def is_palindrome(self, text):
        return text == text[::-1]

    def generate_subsequences(self):
        subsequences = []

        for mask in range(1, 1 << self.n):
            sub = ""
            for i in range(self.n):
                if mask & (1 << i):
                    sub += self.s[i]
            subsequences.append(sub)

        return subsequences

    def get_distinct_palindromes(self):
        self.validate_input()
        palindromes = set()

        for sub in self.generate_subsequences():
            if self.is_palindrome(sub):
                palindromes.add(sub)

        return palindromes


# -------- Main Program --------
try:
    s = input("Enter a string: ")
    counter = PalindromicSubsequenceCounter(s)

    palindromes = counter.get_distinct_palindromes()

    print("\nTotal number of distinct palindromic subsequences:", len(palindromes))
    print("\nDistinct Palindromic Subsequences:")
    for p in sorted(palindromes):
        print(p)

except ValueError as ve:
    print("Input Error:", ve)

except Exception as e:
    print("Unexpected Error:", e)