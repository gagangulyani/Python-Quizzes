"""
Can you guess the output of
the following Python 🐍 Snippet?

Options
=========

1. 1
2. 1.0
3. 2
4. 2.0
"""

a = 10 and 1
b = 0 or 1
print(a + b ** 2)

"""
Solution
=========

3. 2

Explaination:
    >>> (10 and 1) + (0 or 1) ** 2
    
    * Here, when we use "and", the second value will return if
    * first one is true, else the first one is returned
    
    * when we use "or", the first value will return if it is true,
    * else the second value
    
    >>> 1 + (1 ** 2) # Operator Precedence
    
    >>> 1 + 1
    
    >>> 2

For more Pythonic 🐍 Content, find me on Twitter @GaganGulyani
"""