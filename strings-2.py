# Python Quiz #5
# Can you guess the output of the following snippet?

s = f"Pytho\n"
s2 = r"Pytho\n"

print(s)
print(s2)

"""
Options
=========

A) Pytho\n
   Pytho

B) Pytho
   
   Pytho\n
   
C) Syntax Error

D) Pytho

   Pytho
   
Solution
=========

B) Pytho
   
   Pytho\n

Explanation
============

=> \n is an escape sequence (new line)

=> f-strings (s) don't do anything special for escape sequences,
they will be interprated as escape sequence is.

=> raw stings (s1) ignore don't interpret escape sequences.

Therefore...

=> output of print(s):
Pytho


=> output of print(s1):
Pytho\n
"""
