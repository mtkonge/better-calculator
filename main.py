from enum import Enum
from typing import List
from Token import Token, TokenType

from parser import Parser



DIGITS = "0123456789"

def tokenize(text: str) -> List[Token]:
    tokens: List[Token] = []
    i = 0
    while i < len(text):
        if text[i] in " \n\t\r":
            i += 1
        elif text[i] == "+":
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
        else:
            raise Exception(f"expected +-*/(){DIGITS}, got '{text[i]}'")
            
    tokens.append(Token(TokenType.EOF, ""))
    return tokens

def main():
    while True:
        text = input("> ")
        tokens = tokenize(text)
        ast = Parser(tokens).parseExpr()
        print(ast.calculate())

if __name__ == "__main__":
    main()
