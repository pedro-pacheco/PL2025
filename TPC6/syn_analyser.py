from lex_analyser import lexer

next_token = ("Error", '', 0, 0)

expression = []

def parserError(symbol):
    print("Syntax error, unexpected token: ", symbol)

def rec_term(symbol):
    global next_token
    v = next_token.value
    flag = True                     #checks to see if no errors occur
    if next_token.type == symbol:
        next_token = lexer.token()
    else:
        parserError(next_token)
        flag = False
    #checks to see if a number follows an operator
    if symbol in ["ADD", "SUBT", "MULT", "DIV"]:
        if next_token.type != "NUMBER":
            parserError(next_token)
            flag = False
    
    if flag:
        expression.append(v)

# P1: Exp --> Number ExpreCont
# P2: ExpreCont --> '+' Number ExpressCont 
# P3: ExpreCont --> '-' Number ExpressCont
# P4: ExpreCont --> '*' Number ExpressCont
# P5: ExpreCont --> '/' Number ExpressCont
def rec_ExpreCont():
    global next_token
    while next_token:
        if next_token.type == 'NUMBER':
            print("Derivando por P1: Exp --> Number ExpreCont")
            rec_term('NUMBER')
            print("Reconheci P1: Exp --> Number ExpreCont")
        if next_token and next_token.type == 'ADD':
            print("Derivando por P2: ExpreCont --> '+' Number ExpressCont")
            rec_term('ADD')
            print("Reconheci P2: ExpreCont --> '+' Number ExpressCont")
        elif next_token and next_token.type == 'SUBT':
            print("Derivando por P3: ExpreCont --> '-' Number ExpressCont")
            rec_term('SUBT')
            print("Reconheci P3: ExpreCont --> '-' Number ExpressCont'")
        elif next_token and next_token.type == 'MULT':
            print("Derivando por P4: ExpreCont --> '*' Number ExpressCont")
            rec_term('MULT')
            print("Reconheci P4: ExpreCont --> '*' Number ExpressCont")
        elif next_token and next_token.type == 'DIV':
            print("Derivando por P5: ExpreCont --> '/' Number ExpressCont")
            rec_term('DIV')
            print("Reconheci P5: ExpreCont --> '/' Number ExpressCont")
        elif not next_token:
            break
        else:
            parserError(next_token)
    
def rec_Parser(data):
    global next_token
    lexer.input(data)
    next_token = lexer.token()
    rec_ExpreCont()
    print("That's all folks!")

#multiplies and divides the integers in a list separated by * and / signs
def calculate_priority(exp):
    i = 0
    while i < len(exp):
        if exp[i] in ["*", "/"]:
            if exp[i] == '*':
                acc = exp[i-1] * exp[i+1]
            else:
                acc = exp[i-1] / exp[i+1]
            exp[i-1] = acc
            del exp[i]
            del exp[i]
            i-=1
        i+=1
    return exp

#adds and subtracts the integers in a list separated by + and - signs
def calculate_normal(exp):
    i = 0
    while i<len(exp):
        if exp[i] in ["+", "-"]:
            if exp[i] == "+":
                acc = exp[i-1] + exp[i+1]
            else:
                acc = exp[i-1] - exp[i+1]
            exp[i-1] = acc
            del exp[i]
            del exp[i]
            i-=1
        i+=1
        
    return exp

#calculates the arithmetic value of the expression entered
def calculate():

    res = calculate_normal(calculate_priority(expression))

    print("Arithmetic result: ", res[0])

def main():

    line = input("Introduza uma EXPRESSAO: ")
    rec_Parser(line)
    calculate()

if __name__ =="__main__":
    main()