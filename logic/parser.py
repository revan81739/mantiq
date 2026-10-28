from logic.ast import Identifier, Not, Binary

class Parser:
    def __init__(self, tokens):
        self.tokens=tokens
        self.position=0
    def current(self):
        if self.position >=len(self.tokens):
            return None
        return self.tokens[self.position]
    def advance(self):
        self.position+=1
    def parse(self):
        return self.expression()
    def expression(self):
        token=self.current()
        if token is None:
            return None
        if token.token_type=="NOT":
            self.advance()
            return Not(self.expression())
        if token.token_type=="IF":
            self.advance()
            left=self.expression()
            if self.current().token_type!="THEN":
                raise ValueError("expected THEN")
            self.advance()
            right=self.expression()
            return Binary(left, "IMPLIES", right)
        if token.token_type=="IDENTIFIER":
            left=Identifier(token.value)
            self.advance()
            token=self.current()
            if token is None:
                return left
            if token.token_type in ("AND", "OR"):
                operator=token.token_type
                self.advance()
                right=self.expression()
                return Binary(left, operator, right)
            return left
        raise ValueError(f"Unexpected token {token.token_type}")
        
