
from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter.interpreter import Interpreter


def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error

    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter()
    result = interpreter.visit(ast)
    return result, None
