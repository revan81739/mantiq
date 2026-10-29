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
            return self.get_variable(node.oparand)
        if isinstance(node, Binary):
            return (
                self.get_varibles(node.left)
                |
                self.get_variables(node.right)
            )
        return set()
    def verify(self, tree):
        variables=sorted(self.get_variables(tree))
        results=[]

        for values in product([False, True], repeat=len(variables)):
                              assignment=dict(zip(variables, values))
                              result=self.evaluator.evaluate(tree, assignment)
                              results.append((assignment, results))
        return results

        
