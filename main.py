
from enum import Enum
from typing import List

class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    NEGATIVE = 7

class Token:
    def __init__(self, tt: TokenType, value: str):
        self.tt = tt
        self.value = value
    
    def __str__(self) -> str:
        return f"({self.tt}, \"{self.value}\""
    
DIGITS = "0123456789"

def tokenize(text: str) -> List[Token]:
    tokens: List[Token] = []
    i = 0
    willBeNegative = True
    while i < len(text):
        if text[i] in " \n\t\r":
            i += 1
        elif text[i] == "+":
            tokens.append(Token(TokenType.PLUS, text[i]))
            i += 1
            willBeNegative = True
        elif text[i] == "-":
            if willBeNegative:
                tokens.append(Token(TokenType.NEGATIVE, text[i]))
            else:
                tokens.append(Token(TokenType.MINUS, text[i]))
            i += 1
            willBeNegative = True
        
        elif text[i] == "*":
            tokens.append(Token(TokenType.MULTIPLY, text[i]))
            i += 1
            willBeNegative = True
        elif text[i] == "/":
            tokens.append(Token(TokenType.DIVIDE, text[i]))
            i += 1
            willBeNegative = True
        elif text[i] == "(":
            tokens.append(Token(TokenType.LPAREN, text[i]))
            i += 1
            willBeNegative = False

        elif text[i] == ")":
            tokens.append(Token(TokenType.RPAREN, text[i]))
            i += 1
            willBeNegative = True
        elif text[i] in DIGITS:
            value = text[i]
            i += 1
            willBeNegative = False
            while i < len(text) and text[i] in DIGITS:
                value += text[i]
                i += 1
            tokens.append(Token(TokenType.NUMBER, value))
        else:
            raise Exception(f"bruh you fucked up, computer no like '{text[i]}'")
    return tokens

class Expr():
    def __init__(self):
        pass

class Int(Expr):
    def __init__(self, value: int):
        super().__init__()
        self.value = value
    
    def __str__(self) -> str:
        return f"Int {{ value: {self.value} }}"

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.i = 0

    def parseExpr(self) ->  Expr:
        return self.parseVal()
    
    def parseAddOrSub(self) -> Expr:
        pass    

    def mulOrDiv(self) -> Expr:
        pass

    def parseNeg(self) -> Expr:
        if self.tokens[self.i].tt == TokenType:
            pass

    #fn parse_negation() -> Expr {
    #if let current_token() = TokenType::Minus {
    #    let value = parse_negation();
    #    return Expr::Negate(value);
    #} else {
    #    return parse_grouping();
    #}
#}


    def parseGrp(self) -> Expr:
        if self.tokens[self.i].tt == TokenType.LPAREN:
            value = parseNeg()
            self.skip(TokenType.RPAREN)
            return self.parseNeg()
        else:
            return parseVal();

    def parseVal(self) -> Expr:
        if self.tokens[self.i].tt == TokenType.NUMBER:
            value = int(self.tokens[self.i].value)
            expr = Int(value)
            self.i += 1
            return expr
        else:
            raise Exception(f"Expected value, got {self.tokens[self.i]}")

    def skip(self, tokenType: TokenType):
        if self.tokens[self.i].tt == tokenType:
            i += 1
        
def main():
    with open("test.txt") as f:
        text = f.read()
        tokens = tokenize(text)
        for token in tokens:
            print(token)
        ast = Parser(tokens).parseExpr()
        
        print(str(ast))

if __name__ == "__main__":
    main()
