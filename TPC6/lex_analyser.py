import ply.lex as lex

tokens = (
    "NUMBER",
    "ADD",
    "SUBT",
    "MULT",
    "DIV"
)

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#regular expressions for the tokens
t_ADD = r"\+"
t_MULT = r"\*"
t_SUBT = r"\-"
t_DIV = r"\/"

t_ignore = " \t\n"

#rule for errors
def t_error(t):
    print(f"Invalid symbol at line {t.lineno}: {t.value[0]}")       #printing invalid symbol
    t.lexer.skip(1)                                                 #skips invalid symbol

lexer = lex.lex()