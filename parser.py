
from typing import List

from Token import Token, TokenType


class Expr():
    def __init__(self):
        pass

class Int(Expr):
    def __init__(self, value: int):
        super().__init__()
        self.value = value
    
    def __str__(self) -> str:
        return f"Int {{ value: {self.value} }}"

    def toEquation(self) -> str:
        return f"{self.value}"
    
    def calculate(self) -> int:
        return self.value


class Negate(Expr):
    def __init__(self, value: Int):
        super().__init__()
        self.value = value
    def __str__(self) -> str:
        return f"Negate {{ {self.value} }}"

    def toEquation(self) -> str:
        return f"-{self.value.toEquation()}"

    def calculate(self) -> int:
        return -self.value.calculate()
        
class Sub(Expr):
    def __init__(self, left: Int | Negate, right: Int | Negate):
        super().__init__()
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return f"Sub {{ Left: {self.left} Right: {self.right} }}"
    
    def toEquation(self) -> str:
        return f"({self.left.toEquation()} - {self.right.toEquation()})"

    def calculate(self) -> int:
        return self.left.calculate() - self.right.calculate()

        

class Add(Expr):
    def __init__(self, left: Int | Negate, right: Int | Negate):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"Add {{ Left: {self.left} Right: {self.right} }}"

    def toEquation(self) -> str:
        return f"({self.left.toEquation()} + {self.right.toEquation()})"

    def calculate(self) -> int:
        return self.left.calculate() + self.right.calculate()
        

class Mul(Expr):
    def __init__(self, left: Int | Negate, right: Int | Negate):
        super().__init__()
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return f"Mul {{ Left: {self.left} Right: {self.right} }}"

    def toEquation(self) -> str:
        return f"({self.left.toEquation()} * {self.right.toEquation()})"
    
    def calculate(self) -> int:
        return self.left.calculate() * self.right.calculate()

        

class Div(Expr):
    def __init__(self, left: Int | Negate, right: Int | Negate):
        super().__init__()
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return f"Div {{ Left: {self.left} Right: {self.right}}}" 

    def toEquation(self) -> str:
        return f"({self.left.toEquation()} / {self.right.toEquation()})"      
    
    def calculate(self) -> int:
        return self.left.calculate() / self.right.calculate()
        

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.i = 0
        

    def parseExpr(self) ->  Expr:
        return self.parseAddOrSub()
    
    def parseAddOrSub(self) -> Expr:
        left = self.parseMulOrDiv()
        if self.tokens[self.i].tt == TokenType.PLUS:
            self.i += 1
            right = self.parseAddOrSub()
            return Add(left, right)
        elif self.tokens[self.i].tt == TokenType.MINUS:
            self.i += 1
            right = self.parseAddOrSub()
            return Sub(left, right)
        else:
            return left

    def parseMulOrDiv(self) -> Expr:
        left = self.parseNeg()
        if self.tokens[self.i].tt == TokenType.MULTIPLY:
            self.i += 1
            right = self.parseMulOrDiv()
            return Mul(left, right)
        if self.tokens[self.i].tt == TokenType.DIVIDE:
            self.i += 1
            right = self.parseMulOrDiv()
            return Div(left, right)
        else:
            return left

    def parseNeg(self) -> Expr:
        if self.tokens[self.i].tt == TokenType.MINUS:
            self.i += 1
            value = self.parseNeg()
            return Negate(value)
        else:
            return self.parseGrp()


    def parseGrp(self) -> Expr:
        if self.tokens[self.i].tt == TokenType.LPAREN:
            self.i += 1
            value = self.parseExpr()
            self.expect(TokenType.RPAREN)
            self.i += 1
            return value
        else:
            return self.parseVal();

    def parseVal(self) -> Expr:
        if self.tokens[self.i].tt == TokenType.NUMBER:
            value = int(self.tokens[self.i].value)
            expr = Int(value)
            self.i += 1
            return expr
        else:
            raise Exception(f"Expected TokenType.NUMBER, got {self.tokens[self.i]}")

    def expect(self, tokenType: TokenType):
        if self.tokens[self.i].tt != tokenType:
            raise Exception(f"{{expected {self.tokens[self.i].tt}}} ")
        