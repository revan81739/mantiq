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

    def match(self, *types):
        token=self.current()
        if token and token.token_type in types:
            self.advance()
            return token
        return None

    def expect(self, token_type):
        token=self.current()
        if token is None or token.token_type != token_type:
            raise ValueError(f"Expected {token_type}")
        self.advance()
        return token
    
    def parse(self):
        return self.parse_implication()

    def parse_implication(self):
        if self.match("IF"):
            left=self.parse_or()
            self.expect("THEN")
            right=self.parse_implication()
            return Binary(left, "IMPLIES", right)
        return self.parse_or()

    def parse_or(self):
        node = self.parse_and()
        while self.match("OR"):
            right =self.parse_and()
            node = Binary(node, "OR", right)
        return node

    def parse_and(self):
        node=self.parse_not()
        while self.match("AND"):
            right=self.parse_not()
            node=Binary(node, "AND", right)
        return node

    def parse_not(self):
        if self.match("NOT"):
            return Not(self.parse_not())
        return self.parse_primary()

    def parse_primary(self):
        token=self.expect("IDENTIFIER")
        return Identifier(token.value)
    