# Mantiq
Mantiq is a desktop logical reasoning machine thats themed around an antique punch-card based computer

# Features
## Logical argument verification
Evaluates propositional logic arguments using one or more premises and a conclusion. Supported operators 
include and, or, not, if..then, iff(biconditionals), xor, nand, nor, aswell as parentheses for grouping.

## Natural language explanations
For valid arguments, the machine describes why the conclusion follows a set of premises
For invalid arguments, a counterexample is given

![](https://github.com/user-attachments/assets/d6f28068-0c30-4d5d-abf9-947d88863e0d)

## Truth table generator
If you want to delve deeper into the logic behind an argument, the truth table generator can help visualize that

![](https://github.com/user-attachments/assets/f41475c6-fec9-4bb6-828d-06ab042e2ce5)

## Punch card library
A set of classic examples in propositional logic for you to experiment with

![](https://github.com/user-attachments/assets/1e6715f8-232a-4f09-b61c-8146f5455e81)

# Installation and running
The release build can be found [here](https://github.com/revan81739/mantiq/releases/tag/v1.0)

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

If you are new to propositional logic, these are some great places to start:
https://youtu.be/1UmPbfuGfKk?si=vlHrMyvM1xhXSnNZ -basics of Aristotle's logic
https://www.geeksforgeeks.org/engineering-mathematics/proposition-logic/ -if you want to delve deeper


# Notes
So this was only a basic version because a lot of time was spent learning propositional logic, AST's, and some tkinter aswell. Maybe in future ill add predicate logic, more ui effects, and **maybe** nlp so the user can input true human statements. who knows though. have a great day
