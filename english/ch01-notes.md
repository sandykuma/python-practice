# Python Basics — Chapter 1 | Python Full Course — Study Notes

# Python Basics — Chapter 1: Expressions, Data Types, and Variables

This chapter introduces the fundamental building blocks of Python, treating the language as a powerful calculator and a tool for managing data through variables.

### Key Concepts

*   **Math Operators**:
    *   `+` (Addition), `-` (Subtraction), `*` (Multiplication)
    *   `/` (True Division): Always returns a **float** (e.g., `7 / 2 = 3.5`).
    *   `//` (Floor Division): Rounds down to the nearest whole number (e.g., `7 // 2 = 3`).
    *   `%` (Modulus): Returns the remainder of a division (e.g., `7 % 2 = 1`).
    *   `**` (Exponentiation): Calculates power (e.g., `2 ** 3 = 8`).
*   **Order of Operations**: Follows PEMDAS (Parentheses $\rightarrow$ Exponents $\rightarrow$ Multiplication/Division $\rightarrow$ Addition/Subtraction).
*   **Basic Data Types**:
    *   `int`: Whole numbers (Integers).
    *   `float`: Decimal numbers (Floating point).
    *   `str`: Text wrapped in single or double quotes (Strings).
*   **String Manipulation**:
    *   **Concatenation**: Joining strings using `+` (e.g., `"Hello " + "World"`).
    *   **Replication**: Repeating strings using `*` with an integer (e.g., `"Hi! " * 3`).
*   **Variables**:
    *   Used to store values for later use via the assignment operator (`=`).
    *   **Naming Rules**: Must start with a letter or underscore; no spaces or special characters; case-sensitive.
*   **Basic Functions**:
    *   `print()`: Displays output to the screen.
    *   `input()`: Captures user input (always returns data as a **string**).

### Code Examples

**1. Math and Type Promotion**
```python
a = 5       # int
b = 2.5     # float
result = a + b 
print(result) 
# Output: 7.5 (int is promoted to float)
```

**2. String Operations**
```python
name = "Ravi"
greeting = "Hello, " + name # Concatenation
echo = "Hi! " * 3           # Replication
print(greeting)
print(echo)
# Output: Hello, Ravi
# Output: Hi! Hi! Hi! 
```

**3. Simple User Interaction**
```python
user_name = input("Enter your name: ")
# input() returns a string, so we convert age to int for math
user_age = int(input("Enter your age: ")) 
print("Hello " + user_name + "!")
print("Next year you will be " + str(user_age + 1))
# Example Output: 
# Enter your name: Alice
# Enter your age: 21
# Hello Alice!
# Next year you will be 22
```

### Common Mistakes
*   **TypeError**: Trying to concatenate a string and an integer directly (e.g., `"Age: " + 21`). Use `str()` to convert the number or use f-strings.
*   **Variable Naming**: Using spaces or starting a variable name with a number (e.g., `user name` or `1variable`), which causes a `SyntaxError`.
*   **Division Confusion**: Using `/` when you specifically need a whole number (integer) result; use `//` instead.

**Summary:** Python uses standard math operators, supports dynamic data types (`int`, `float`, `str`), and stores data in case-sensitive variables for program logic.
