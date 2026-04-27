# Python_master07
#1. basics_void_functions.py
# 1. Factorial using a loop 
def factorial():
    n = 5
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print("Factorial:", fact)

# 2. Prime Number Check 
def prime():
    n = 7
    flag = True
    if n <= 1:
        flag = False
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    print("Prime" if flag else "Not Prime")

# 3. Fibonacci Series 
def fibonacci():
    a, b = 0, 1
    print("Fibonacci:", end=" ")
    for i in range(7):
        print(a, end=" ")
        a, b = b, a + b
    print()

# 4. Palindrome Number Check 
def palindrome():
    n = 121
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    if original == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

# 5. Armstrong Number Check 
def armstrong():
    n = 153
    temp = n
    sum_val = 0
    while temp > 0:
        digit = temp % 10
        sum_val += digit ** 3
        temp //= 10
    if sum_val == n:
        print("Armstrong")
    else:
        print("Not Armstrong")

# 6. Multiplication Table 
def table():
    n = 5
    print("Table of", n)
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

# 7. Largest of Three Numbers 
def largest():
    a, b, c = 10, 25, 15
    if a > b and a > c:
        print("Largest:", a)
    elif b > c:
        print("Largest:", b)
    else:
        print("Largest:", c)

# 8. Even or Odd 
def even_odd():
    n = 8
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

# 9. Simple Interest 
def simple_interest():
    p, r, t = 1000, 5, 2
    si = (p * r * t) / 100
    print("Simple Interest:", si)

# Running the functions
if __name__ == "__main__":
    factorial()
    prime()
    fibonacci()
    palindrome()
    armstrong()
    table()
    largest()
    even_odd()
    simple_interest() 
#2. functional_logic.py
# Factorial with return value 
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

# Prime check with boolean return 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Fibonacci with parameter 
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Palindrome with logic 
def is_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return original == rev

# Armstrong number logic 
def is_armstrong(n):
    sum_val = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_val += digit ** 3
        temp //= 10
    return sum_val == n

# Largest of three with return 
def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

# Sum of digits logic 
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Examples of usage
print("Factorial of 5:", factorial(5)) 
print("Is 121 Palindrome?:", is_palindrome(121))
print("Sum of digits of 1234:", sum_of_digits(1234)) 
#3. oop_concepts.py
# 1. Rectangle Area Class 
class Rectangle:
    def set_values(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Area:", self.length * self.width)

# 2. Employee Details Class 
class Employee:
    def get_data(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

# 3. Calculator Class
class Calculator:
    def add(self, a, b):
        print("Sum:", a + b)
    def sub(self, a, b):
        print("Difference:", a - b)

# 4. Student Marks Class 
class Student:
    def get_marks(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def total(self):
        print("Total:", self.m1 + self.m2)

# Implementation examples
rect = Rectangle()
rect.set_values(5, 3)
rect.area() 

emp = Employee()
emp.get_data("Rahul", 50000)
emp.display() 

calc = Calculator()
calc.add(10, 5)
