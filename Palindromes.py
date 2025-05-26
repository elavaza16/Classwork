#Using stacks to check if a word is a palindrome

class Palindromes:
    def _init_(self):
        self.stack=[]
    #Push the characters into a stack
    def push(self,characters):
        self.stack.append(characters)

    def pop(self):
        return  self.stack.pop()

def is_palindrome(s):

    check=Palindromes()

    for char in s:
        check.push(char)

    for i in range(len(s) //2):
        if check.pop()!=s[i]:
         return False
    return True


s=input("Enter a word:\n").strip()
#To abide by the constraints given
if not (1<=len(s)<=50):
    print("This value is bot allowed")
    exit()
if is_palindrome(s):
    print(f"The word is, {s}, is a palindrome.")

else:
    print(f"The word is, {s}, is not palindrome.")