from dataclasses import dataclass

class Node:
    pass

@dataclass 
class Identifier(Node):
    name:str

@dataclass
class Not(Node):
    operand: Node

@dataclass
class Binary(Node):
    left: Node
    operator:str
    right:Node

