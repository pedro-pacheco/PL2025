import re
import ply.lex as lex

tokens = (
    "NUMBER",           #NUMBERS
    "SELECT",
    "WHERE",
    "LIMIT",
    "A",
    "LCURLY",           #OPEN CURLY BRACKETS
    "RCURLY",           #CLOSE CURLY BRACKETS
    "DOT",              #DOT TO CLOSE STATEMENT
    "VARIABLE",         #ANY VARIABLE NAME STARTS WITH ?
    "PREDICATE",        #CONTAINS : OUTSIDE QUOTES
    "NAMEDOBJECTS",     #BETWEEN QUOTES
    "SPECIFICATION"     #BEGINS WITH @
)

#regular expressions for tokens
t_SELECT = r"[Ss][Ee][Ll][Ee][Cc][Tt]"
t_WHERE = r"[Ww][Hh][Ee][Rr][Ee]"
t_LIMIT = r"[Ll][Ii][Mm][Ii][Tt]"
t_A = r"[Aa]"
t_LCURLY = r"\{"
t_RCURLY = r"\}"
t_DOT = r"\."
t_VARIABLE = r"\?\w+"
t_PREDICATE = r"(?<!\")\w+:\w+(?=[ .,;])"           #space followed by word followed by : followed by word followed by space
t_NAMEDOBJECTS = r'".+"'
t_SPECIFICATION = r"@\w+"

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#characters to ignore
t_ignore = " \t" 

#rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#rule for errors
def t_error(t):
    print(f"Invalid symbol at line {t.lineno}: {t.value[0]}")       #printing invalid symbol
    t.lexer.skip(1)         #faz skip ao símbolo que dá erro


def analyser(inputString):

    lexer = lex.lex()
    lexer.input(inputString)

    while r:= lexer.token():
        print(r)

def main():
    input_text = ""
    flag = True             #flag that determines whether you keep reading from input

    while flag:
        line = input().strip()
        if line == "EXIT":
            flag = False
        else:
            input_text=input_text + line
    
    analyser(input_text)
        
if __name__ == "__main__":
    main()