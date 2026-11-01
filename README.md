# Mantiq
Mantiq is a desktop logical reasoning machine thats themed around an antique punch-card based computer

# Features
## Logical argument verification
Evaluates propositional logic arguments using one or more premises and a conclusion. Supported operators 
include and, or, not, if..then, iff(biconditionals), xor, nand, nor, aswell as parentheses for grouping.
## Natural language explanations
For valid arguments, the machine describes why the conclusion follows a set of premises
For invalid arguments, a counterexample is given
## Truth table generator
If you want to delve deeper into the logic behind an argument, the truth table generator can help visualize that
## Punch card library
A set of classic examples in propositional logic for you to experiment with

# Installation and running
The release build can be found here.

# Writing arguments
Arguments are written one premise per line
The final line must begin with the keyword "Verify"
Example:
If P Then Q
P
Verify Q

Example with parentheses:
(P Or Q) And Not R
Verify P Or Q

If you are new to propositional logic, these places are great to start with-

# Notes
So this was only a basic version because a lot of time was spent learning propositional logic, AST's, and some tkinter aswell. Maybe in future ill add predicate logic, more ui effects, and **maybe** nlp so the user can input true human statements. who knows though. have a great day
