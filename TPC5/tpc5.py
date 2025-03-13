import json
import ply.lex as lex
from datetime import datetime
import sys

tokens = (
    "LIST",
    "COIN",
    "SELECT",
    "EXIT",
    "PRODUCTCODE",
    "AMOUNT",
    "ADD"           #ADMINISTRATOR ADD PRODUCT
)

#regular expressions for tokens
t_LIST = r"LIST"
t_SELECT = r"SELECT"
t_EXIT = r"EXIT"
t_COIN = r"COIN"
t_PRODUCTCODE = r"[A-Z]\d+"
t_AMOUNT = r"((((1|2)e)|(50|20|10|5)c)(, )?)+"
    
#characters to ignore
t_ignore = " \t\n" 

#rule for errors
def t_error(t):
    print(f"Invalid symbol at line {t.lineno}: {t.value[0]}")       #printing invalid symbol
    t.lexer.skip(1)                                                 #skips invalid symbol

def convertmoneytoken(tok):
    am = tok.split(",")[0]
    match am[-1]:
        case "e":
            v = int(am[:-1])
        case "c":
            v = int(am[:-1])*0.01
    return v

def update_stock(stock, balance, cd):
    if(balance > stock[cd][2]):             #if enough money was inserted
        if(stock[cd][1]>0):                 #if enough quantity is available
            item = list(stock[cd])
            item[1]-=1
            stock[cd]=tuple(item)
            balance-=stock[cd][2]
            balance = round(balance, 2)     #rounding balance
            print(f"Selected {stock[cd][0]}")
            print("...")
            print("You may pick up selected item from the tray")
            print(f"Remaining balance: {balance}")
        else:
            print("Product unavailable")
    else:
        print("Not enough money")
        print(f"Remaining balance: {balance}")
    
    return stock, balance

def get_change(balance):
    change = {}
    coins = [2, 1, 0.5, 0.2, 0.1, 0.05]
    for coin in coins:
        change[coin] = int(balance // coin)
        balance = round(balance % coin, 2)

    coins = [(key, value) for key, value in change.items() if value >0]
    goodbye_message = "You may remove your change: "
    for (x, y) in coins:
        m = (f"{y}x{x}€, ")
        goodbye_message = goodbye_message + m

    goodbye_message = goodbye_message[:-2]       
    print(goodbye_message)    


def main():

    input = open("vending_machine_stock.json", "r", encoding="utf-8")
    data = json.load(input)
    stock = {}
    balance = 0.0

    for p in data:
        key = p["code"]
        value = (p["name"], int(p["stock"]), float(p["price"]))
        stock[key] = value

    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lexer = lex.lex()
    print(f"{current_date}, Welcome! I'm ready to fulfil your request")
    for line in sys.stdin:
        lexer.input(line)
        for token in lexer:
            if token.type == "LIST":
                print(f"{'code' : <5}|{'Name' : ^22}|{'Quantity' : ^10}|{'Price' : >5}")
                print("---------------------------------------------------")
                for key, value in stock.items():
                    print(f"{key : <5}|{value[0] : ^22}|{value[1] : ^10}|{value[2] : .2f}")
            elif token.type == "COIN":
                while am:= lexer.token():
                    if am != None:          #check for errors
                        res = convertmoneytoken(am.value)
                        balance += res
                print(f"You have inserted: {balance}")
            elif token.type == "SELECT":
                cd = lexer.token().value
                if cd in stock:             #product available in the database
                    stock, balance = update_stock(stock, balance, cd)
                else:                       #product not available in the database
                    print("Selected Product not found")
            
            elif token.type == "EXIT":
                if(balance>0):
                    get_change(balance)
                    balance = 0.0
                print("Until next time!")
                return 0

if __name__ =="__main__":
    main()