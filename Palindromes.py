import re
class Palindrome:
    def __init__(self):
        self.stack = []

    def push(self, ch):
        self.stack.append(ch)

    def pop(self):
        return self.stack.pop()


# Create the Solution object
def is_palindrome(ch):
    #Clean the string  by removing characters not letters or digits and convert the string to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', ch).lower()
    obj = Palindrome()
    for ch in cleaned:
        obj.push(ch)

    for i in range(len(cleaned) // 2):
        if obj.pop() != cleaned[i]:
            return False
    return True


if __name__=="__main__":
    # Output result
    s = input("Enter a word to check if it's a palindrome: ").strip()
    if not (1 <= len(s) <= 50):
        raise ValueError("Input string length must be between 1 and 50.")
    if is_palindrome(s):
        print(f"The word, {s}, is a palindrome.")
    else:
        print(f"The word, {s}, is not a palindrome.")