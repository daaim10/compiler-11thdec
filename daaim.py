import re

# Define token specifications
token_specs = [
    # Data Types
    ('INT', r'\b(adad_saheh)\b'),         # int
    ('FLOAT', r'\b(adad_ashari)\b'),      # float
    ('STRING', r'\b(silsila)\b'),         # string
    ('BOOLEAN', r'\b(dugana)\b'),         # boolean 

    # Control Flow
    ('WHILE', r'\b(jab_tak)\b'),          # while
    ('IF', r'\b(agar)\b'),                # if
    ('ELSE', r'\b(warna)\b'),             # else
    ('ELIF', r'\b(warna_agar)\b'),        # elif

    # Loops
    ('FOR', r'\b(chalo)\b'),
    ('TILL',r'\b(se)\b'),       # for

    # Operators
    ('PLUS', r'\b(jama)\b'),              # +
    ('MINUS', r'\b(manfi)\b'),            # -
    ('MULTIPLY', r'\b(zarb)\b'),          # *
    ('DIVIDE', r'\b(taqseem)\b'),         # /
    ('LESS_THAN', r'\b(kam_hai)\b'),      # <
    ('GREATER_THAN', r'\b(zyada_hai)\b'), # >
    ('GREATER_EQUAL', r'\b(zyada_ya_barabr_hai)\b'), # >=
    ('LESS_EQUAL', r'\b(kam_ya_barabr_hai)\b'),      # <=
    ('EQUALS', r'\b(barabr_hai)\b'),       # = 
    ('NOT_EQUAL', r'\b(barabr_nhi_hai)\b'), # !=
    ('EXACTLY_EQUAL_TO',r'\b(bilkul_barabr_hai)\b'), # ==

    # Match number (integer or float)
    ('NUMERIC_VALUE',r'\b(\d+(\.\d+)?)\b'),  # Match integers and floats (e.g., 42, 3.14)

    # Match string values
    ('STRING_VALUE',r'\'[^\']*\'|\"[^\"]*\"'),  # Match strings in single or double quotes (e.g., 'hello', "world")

    # Match boolean values
    ('BOOLEAN_VALUE',r'\b(True|False)\b'),  # Match boolean values True or False

    # Functions
    ('DEF', r'\b(bayan_karo)\b'),         # def
    ('PRINT', r'\b(kaho)\b'),        # print
    ('RETURN',r'\b(wapas)\b'),       # return

    # Function call pattern (matches function names followed by parentheses)
    ('FUNC_CALL', r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\((.*?)\)'),  # Matches function call: func_name(params)
    
    # Parenthesis tokens
    ('LPAREN', r'\('),  # Left parenthesis
    ('RPAREN', r'\)'),  # Right parenthesis

    # Variable names (identifiers)
    ('NAMING_VARIABLE',r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'),  # Matches variables

    # Skip whitespace and newline
    ('SKIP', r'[ \t]+'),                  # whitespace
    ('NEWLINE', r'\n'),                   # newline
    ('COLON', r':'),

    # Catch-all for any non-matching characters
    ('COMMENT', r'#.*'),
    ('MISMATCH', r'.'),
    # Skip comments starting with #

]

# Create the master pattern
master_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specs)

def tokenize():
    tokens = []
    line_number = 1  # Start from line 1

    print("Enter your code (type 'END' on a new line to finish):")
    user_input = []
    
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        user_input.append(line)
    code = "\n".join(user_input)

    for match in re.finditer(master_pattern, code):
        kind = match.lastgroup   # Name of the matched group (token type)
        value = match.group()    # The actual matched text
        
        if kind in ['SKIP','COMMENT']:
            continue  # Ignore whitespace
        elif kind == 'NEWLINE':
            line_number += 1  # Increment line number on newline
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r} on line {line_number}')
        else:
            tokens.append((line_number, kind, value))  # Include line number, token type, and value

    return tokens

# Sample input to tokenize
# code = """agar(a barabr_hai b):
# kaho 'onn'
# """

# Run the tokenizer
tokens = tokenize()
print("Line # | Class Part        | Value Part")
print("-" * 30)
for line, kind, value in tokens:
    print(f"{line:<4} | {kind:<12} | {value}")
