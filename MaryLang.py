# this file will contain all the code
# TOKENS
DIGITS = '0123456789'
# TOKENS TYPES
TT_INT = "TT_INT"
TT_FLOAT = "TT_FLOAT"
TT_PLUS = "TT_PLUS"
TT_MINUS = "TT_MINUS"
TT_MUL = "TT_MUL"
TT_DIV = "TT_DIV"  # DIDNT MENTION TOO IG
TT_LPAREN = "TT_LPAREN"
TT_RPAREN = "TT_RPAREN"
TT_STRING = "TT_STRING"  # DIDNT MENTIONED IN THE VID BUT WE SUPPOSED TO WORK ON IT
######################## errors CLASS #####################################################################
###################################################################################################################
class errors:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details
    def __str__(self):
        return f'{self.error_name} : {self.details}'
class IllegalCharacterError(errors):
    def __init__(self, details):
        super().__init__('illegal character' ,details)


################################ TOKENS CLASS #######################
#####################################################################
class Tokens :

    def __init__(self, type_, value = None ):
        self.type = type_
        self.value = value
    def __repr__(self):
        if self.value is not None  : return f'({self.type}, {self.value})'
        return f'({self.type})'

############# lexer CLASS #######################
##############################################
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()


    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_numbers())
            elif self.current_char == '\n':
                self.advance()
            elif self.current_char == '+':
                tokens.append(Tokens(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Tokens(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Tokens(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Tokens(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Tokens(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Tokens(TT_RPAREN))
                self.advance()
            else :
                char = self.current_char
                self.advance()
                return [], IllegalCharacterError(f"'{char}'")


        return tokens, None

    def make_numbers(self):
        num_str = ''
        dot_count = 0
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count== 1: break
                dot_count += 1
                num_str += '.'


            else :
                num_str += self.current_char

            self.advance()



        if dot_count == 0:
                return Tokens(TT_INT, int(num_str))
        else :
                return Tokens(TT_FLOAT, float(num_str))


###################################################################################################################
# term --> MUL/DIV
#Expression --> ADD/SUBSTRACT
#Factor--> just the number
# NODES#####
class NumberNode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f'({self.tok})'

#### bin operations
####################### WE STOPPED HEREEEEE
class BinOpNode:
    def __init__(self, leftN,OpTok, rightN):
        self.leftN = leftN
        self.OpTok = OpTok
        self.rightN = rightN
    def __repr__(self):
        return f'({self.leftN} {self.OpTok} {self.rightN})'

###################################################################################################################
######## parser CLASS ######################3
class Parser:
    def __init__(self, tokens):
        self.currentTok = None
        self.tokens = tokens
        self.tok_index= -1
        self.advance()


    def advance(self):
        self.tok_index += 1
        if self.tok_index < len(self.tokens):
            self.currentTok = self.tokens[self.tok_index]
            return self.currentTok
        return None

    ###############################
    ## PARSE METHOD
    def parse(self):
        res = self.expr()
        return res

    def factor(self):
        tok = self.currentTok
        if tok.type in (TT_INT, TT_FLOAT):
            self.advance()
            return NumberNode(tok)
        elif tok.type == TT_LPAREN:
            self.advance()  # Skip the '('
            expr = self.expr()  # Parse the expression inside
            if self.currentTok.type == TT_RPAREN:
                self.advance()  # Skip the ')'
                return expr
            else:
                # Return an error if closing paren is missing
                return None  # Or create a proper error object

    def term(self):
        return self.binop(self.factor, (TT_MUL, TT_DIV))

    def expr(self):
        return self.binop(self.term, (TT_PLUS, TT_MINUS))

    def binop(self, function, operations):
        left = function()
        while self.currentTok and self.currentTok.type in operations:
            op_tok = self.currentTok
            self.advance()
            right = function()
            left = BinOpNode(left, op_tok, right)
        return left


### RUN
def run(text):
    #generate tokens
    lexer = Lexer(text)
    tokenss, error = lexer.make_tokens()
    if error:
        return None, error
    #generate AST
    parser = Parser(tokenss)
    ast = parser.parse()
    interpreter = Interpreter()
    result = interpreter.visit(ast)
    return result, None


###################################################################################################################
###################################################################################################################
class Number :
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

### interpreter ###
class Interpreter:


    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name, self.NoVisit)
        return method(node)

    def NoVisit(self,node):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    def visit_NumberNode(self, node):
        return Number(node.tok.value)
    def visit_BinOpNode(self, node):
        left = self.visit(node.leftN)
        right = self.visit(node.rightN)
        if node.OpTok.type == TT_PLUS:
            return Number(left.value + right.value)
        elif node.OpTok.type == TT_MINUS:
            return Number(left.value - right.value)
        elif node.OpTok.type == TT_MUL:
            return Number(left.value * right.value)
        elif node.OpTok.type == TT_DIV:
            if right.value != 0:
                return Number(left.value / right.value)
            else :
                return "Division by zero"
        return None

#


