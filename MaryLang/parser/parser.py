# from ast_nodes import *
# from ..lexer.tokens_types import *
from parser.ast_nodes import *
from lexer.tokens_types import *



class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_index = -1
        self.currentTok = None
        self.advance()

    def advance(self):
        self.tok_index += 1
        if self.tok_index < len(self.tokens):
            self.currentTok = self.tokens[self.tok_index]
            return self.currentTok
        return None

    def parse(self):
        return self.expr()

    def factor(self):
        tok = self.currentTok

        if tok.type in (TT_INT, TT_FLOAT):
            self.advance()
            return NumberNode(tok)

        elif tok.type == TT_LPAREN:
            self.advance()
            expr = self.expr()
            if self.currentTok.type == TT_RPAREN:
                self.advance()
                return expr

    def term(self):
        return self.binop(self.factor, (TT_MUL, TT_DIV))

    def expr(self):
        return self.binop(self.term, (TT_PLUS, TT_MINUS))

    def binop(self, func, ops):
        left = func()

        while self.currentTok and self.currentTok.type in ops:
            op_tok = self.currentTok
            self.advance()
            right = func()
            left = BinOpNode(left, op_tok, right)

        return left
