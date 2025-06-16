class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
def isPalindrome(input_string):
    
    stack = Stack()
    
    sanitized_string = ''.join(char for char in input_string if char.isalnum()).lower()
    n = len(sanitized_string)
    
    if n == 0:
        return True
    
    midpoint = n // 2
    
    # Push half of string to stack
    for i in range(midpoint):
        stack.push(sanitized_string[i])
    
    start_index_pop = midpoint if n%2==0 else midpoint+1
    
    # check last half of string
    for i in range(start_index_pop, n):
        if sanitized_string[i] == stack.top():
            stack.pop()
            
    # If stack empty, then it is palindrome
    return stack.isEmpty()
    
if __name__ == "__main__":
    string_check = input("Masukkan string untuk dicek : ")
    if(isPalindrome(string_check)):
        print(f'{string_check} adalah Palindrome')
    else:
        print(f'{string_check} bukan Palindrome')
    