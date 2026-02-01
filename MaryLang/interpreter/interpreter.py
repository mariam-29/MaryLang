# from ..lexer.tokens_types import *
from lexer.tokens_types  import *


class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class Interpreter:
    def visit(self, node):
        method = getattr(self, f'visit_{type(node).__name__}', self.no_visit)
        return method(node)

    def no_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')

    def visit_NumberNode(self, node):
        return Number(node.tok.value)

    def visit_BinOpNode(self, node):
        left = self.visit(node.leftN)
        right = self.visit(node.rightN)

        if node.opTok.type == TT_PLUS:
            return Number(left.value + right.value)
        if node.opTok.type == TT_MINUS:
            return Number(left.value - right.value)
        if node.opTok.type == TT_MUL:
            return Number(left.value * right.value)
        if node.opTok.type == TT_DIV:
            if right.value == 0:
                return "Division by zero"
            return Number(left.value / right.value)
