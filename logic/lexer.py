from logic.token import Token

class Lexer:
    keywords={"IF", "THEN", "AND", "OR", "NOT", "VERIFY"}
    
    
    def tokenize(self, text):
        tokens=[]
        for line in text.splitlines():
            words=line.split()
            for word in words:
                word=word.upper()
                if word in self.keywords:
                    tokens.append(Token(word,word))
                else:
                    tokens.append(Token("IDENTIFIER", word))
            tokens.append(Token("NEWLINE", "\n"))
        return tokens
    