class NumberNode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f'({self.tok})'


class BinOpNode:
    def __init__(self, leftN, opTok, rightN):
        self.leftN = leftN
        self.opTok = opTok
        self.rightN = rightN

    def __repr__(self):
        return f'({self.leftN} {self.opTok} {self.rightN})'
