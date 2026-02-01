# MaryLang

A interpreted programming language  written in Python

##  Features

- **Arithmetic Operations**: Supports addition, subtraction, multiplication, and division
- **Parentheses**: Proper operator precedence with parenthetical expressions
- **Integer & Float Support**: Handles both integer and floating-point numbers
- **Interactive REPL**: Command-line shell for testing expressions
- **Modular Architecture**: Clean separation of lexing, parsing, and interpretation phases
-  **MORE COMING SOON**

## 📋 Requirements

- Python 3.6 or higher

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/mariam-29/MaryLang.git
cd MaryLang
```

2. Run the interactive shell:
```bash
python shell.py
```

## 💻 Usage

### Interactive Shell

Launch the REPL by running:
```bash
python shell.py
```

### Example Operations

```
MaryLang > 5 + 3
8

MaryLang > 10 * (2 + 3)
50

MaryLang > 15.5 / 2
7.75

MaryLang > (4 + 6) * (10 - 3)
70
```



## 🏗️ Architecture

The project is organized into a modular structure:

```
MaryLang/
├── .venv/                     # Virtual environment
├── MaryLang/                  # Main package
│   ├── errors/               
│   │   ├── __init__.py
│   │   └── errors.py          # Error handling classes
│   ├── interpreter/
│   │   ├── __init__.py
│   │   └── interpreter.py     # Expression evaluator
│   ├── lexer/
│   │   ├── __init__.py
│   │   ├── constants.py       # Token type constants
│   │   ├── lexer.py          # Lexical analyzer
│   │   ├── tokens.py         # Token class
│   │   └── tokens_types.py   # Token type definitions
│   ├── parser/
│   │   ├── __init__.py
│   │   ├── ast_nodes.py      # Abstract Syntax Tree nodes
│   │   └── parser.py         # Syntax parser
│   └── runner.py             # Main execution function
├── shell.py                   # Interactive REPL
├── Grammer.txt               # Language grammar specification
└── README.md                 # This file
```

### Components

- **Lexer**: Tokenizes input text into meaningful tokens (numbers, operators, parentheses)
- **Parser**: Builds an Abstract Syntax Tree (AST) following operator precedence rules
- **Interpreter**: Traverses the AST and evaluates expressions
- **Error Handling**: Provides clear error messages for illegal characters and syntax errors

## 📝 Grammar

The language follows this grammar structure:

```
expression  : term ((PLUS | MINUS) term)*
term        : factor ((MUL | DIV) factor)*
factor      : INT | FLOAT
            | LPAREN expression RPAREN
```

## 🔧 Development

### Project Structure

Each component has a single responsibility:

- `tokens.py` - Defines token types and the Token class
- `lexer.py` - Converts raw text into tokens
- `ast_nodes.py` - Defines AST node types (NumberNode, BinOpNode)
- `parser.py` - Builds the AST from tokens
- `interpreter.py` - Evaluates the AST
- `errors.py` - Custom error classes
- `runner.py` - Ties everything together

### Adding New Features

To extend MaryLang:

1. **Add new token types** in `tokens.py`
2. **Update the lexer** in `lexer.py` to recognize new tokens
3. **Create new AST nodes** in `ast_nodes.py` if needed
4. **Extend the parser** in `parser.py` to handle new syntax
5. **Implement evaluation logic** in `interpreter.py`

## 🎯 Roadmap

Future features planned:

- [ ] Variable assignment and storage
- [ ] Functions and function calls
- [ ] Control flow (if/else, loops)
- [ ] String operations
- [ ] Boolean logic and comparison operators
- [ ] Comments
- [ ] File execution (run .mary files)
- [ ] Looping (for/while)
- [ ] Error position tracking (line and column numbers)
- [ ] Standard library functions
- [ ] Machine Learning built in library
- [ ] more AI related features

## 🤝 Contributing

Feedback and suggestions are welcomed! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

**Mariam**
- GitHub: [@mariam-29](https://github.com/mariam-29)

## 🙏 Acknowledgments

Built as a learning project to understand compiler/interpreter design and implementation.

---

**Note**: This is an educational project and a work in progress. The language is continuously evolving with new features being added.
