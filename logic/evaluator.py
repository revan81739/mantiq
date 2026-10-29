from logic.ast import Identifier, Not, Binary

class Evaluator:
    def evaluate(self, node, values):
        if isinstance(node, Identifier):
            return values[node.name]
        if isinstance(node, Not):
            return not self.evaluate(node.operand, values)
        if isinstance(node, Binary):
            left = self.evaluate(node.left, values)
            right = self.evaluate(node.right, values)
            if node.operator=="AND":
                return left and right
            if node.operator=="OR":
                return left or right
            if node.operator=="IMPLIES":
                return (not left) or right

        raise ValueError("Unknown node")
        