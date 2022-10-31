
from enum import Enum


class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    EOF = 7

class Token:
    def __init__(self, tt: TokenType, value: str):
        self.tt = tt
        self.value = value
    
    def __str__(self) -> str:
        return f"({self.tt}, \"{self.value}\""
    