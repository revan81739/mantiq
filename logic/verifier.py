from itertools import product

from logic.ast import Identifier, Not, Binary
from logic.evaluator import Evaluator

class Verifier:
    def __init__(self):
        self.evaluator=Evaluator()

    def get_variables(self, node):
        if isinstance(node, Identifier):
            return {node.name}
        if isinstance(node, Not):
            return self.get_variables(node.operand)
        if isinstance(node, Binary):
            return (
                self.get_variables(node.left)
                |
                self.get_variables(node.right)
            )
        return set()
    def get_argument_variables(self, argument):
        variables=set()
        for premise in argument.premises:
             variables |=self.get_variables(premise)
        variables |=self.get_variables(argument.conclusion)
        return variables

    def verify_argument(self, argument):
        variables=sorted(self.get_argument_variables(argument))
        for values in product([False, True], repeat=len(variables)):
            assignment=dict(zip(variables, values))
            premises_true=all(
                self.evaluator.evaluate(
                    premise, 
                    assignment)
                for premise in argument.premises)
            conclusion_true=self.evaluator.evaluate(argument.conclusion, assignment)
            if premises_true and not conclusion_true:
                return False, assignment
        return True, None
    
                
        

        
        

        
            
        
                

        
