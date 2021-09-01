# What is the output of the following
# Python 🐍 Snippet?

a = "World!"
s1 = "{a}"
result = f"Hello, {s1}"
print(result)

"""
Options:
========

1. Hello, World!
2. Hello, {s1}
3. Hello, {{World!}}
4. Hello, {a}


Answer:
=======
4. Hello, {a}


Explaination:
============
    => s1 -> "{a}" (It's not an f-string, it remains untouched)
    => result -> f"Hello, {s1}"
    => "Hello, {a}" ("{s1}" is replaced with value of s1)
"""