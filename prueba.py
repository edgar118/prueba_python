from faker import Faker
fake = Faker()

class Stack:
    def __init__(self, stack):
        self.stack = stack

    def peek(self):
        peek = self.stack[-1]
        return peek
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def enqueue(self, element):
        self.stack.append(element)
        return self.stack
        
    def dequeue(self):
        self.stack.pop()
        return self.stack

class TestPythonDev:
    #Ejercicio 1: invertir una cadena 
    def reverse_word(self, word):
        return word[::-1]

    #Ejercicio 2: palíndromo
    def is_palindrome(self, word):
        return word == self.reverse_word(word)
    
    #Ejercicio 3: cadena de palindromo
    def count_palindromic_substrings(self, word):
        palindrome_list = []
        if self.is_palindrome(word):
            word_len = len(word)
            for longitud in range(1, word_len + 1):
                for group_by_letter in range(word_len - longitud + 1):
                    subcadena = word[group_by_letter:group_by_letter + longitud]
                    if self.is_palindrome(subcadena) and subcadena not in palindrome_list:
                        palindrome_list.append(subcadena)
                
        return len(palindrome_list)
    
    #Ejercicio 4: pila push, pop, peek
    def stack(self):
        fake_names = [fake.name() for _ in range(10)]
        class_stack = Stack(fake_names)

        class_stack.dequeue()
        class_stack.enqueue('German Acevedo')
        class_stack.peek()

    #Ejercicio 5: enqueue y dequeue
    def queue_stack(self):
        fake_names = [fake.name() for _ in range(10)]
        class_stack = Stack(fake_names)

        class_stack.enqueue('German Acevedo')
        class_stack.dequeue()
    
    #Ejercicio 6: check stack with quotation marks
    def check_stack(word):
        class_stack = Stack([])

        for caracter in word:
            if caracter == '(':
                class_stack.enqueue(caracter)
            elif caracter == ')':
                if class_stack.is_empty():
                    return False
                else:
                    class_stack.dequeue()
        return class_stack.is_empty()