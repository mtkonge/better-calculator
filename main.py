
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

class Token:
    def __init__(self, tt: TokenType, value: str):
        self.tt = tt
        self.value = value
    
    def __str__(self) -> str:
        return f"({self.tt}, \"{self.value}\""

DIGITS = "0123456789"

def tokenize(text: str) -> List[Token]:
    tokens: list[object] = []
    i = 0
    isNumber = False
    while i < len(text):
        if text[i] == "+":
            tokens.append(Token(TokenType.PLUS, text[i]))
            i += 1
        elif text[i] == "-":
            tokens.append(Token(TokenType.MINUS, text[i]))
            i += 1
        elif text[i] == "*":
            tokens.append(Token(TokenType.MULTIPLY, text[i]))
            i += 1
        elif text[i] == "/":
            tokens.append(Token(TokenType.DIVIDE, text[i]))
            i += 1
        elif text[i] == "(":
            tokens.append(Token(TokenType.LPAREN, text[i]))
            i += 1
        elif text[i] == ")":
            tokens.append(Token(TokenType.RPAREN, text[i]))
            i += 1
        elif text[i] in DIGITS:
            value = text[i]
            i += 1
            while i < len(text) and text[i] in DIGITS:
                value += text[i]
                i += 1
            tokens.append(Token(TokenType.NUMBER, value))
    return tokens

def main():
    with open("test.txt") as f:
        text = f.read()
        tokens = tokenize(text)
        for token in tokens:
            print(token)

if __name__ == "__main__":
    main()
