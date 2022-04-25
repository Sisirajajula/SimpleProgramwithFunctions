import art
#Add
def add(n1, n2):
  return n1 + n2
#Substraction
def sub(n1, n2):
  return n1 - n2
#Multiplication
def mul(n1, n2):
  return n1 * n2
#Division
def div(n1, n2):
  return n1/n2
def calculator():
    print(art.logo)
    Operations = {'+': add,'-': sub,'*': mul,'/':div}
    num1 = float(input('Enter first number ?'))
    for symbol in Operations:
        print(symbol)
    should_continue = True
    while should_continue:
        Operation_symbol = input('Enter operation symbol to be performed? ')
        num = float(input('Enter next number ?'))
        OperationPerformed = Operations[Operation_symbol]
        answer = OperationPerformed(num1,num)
        print(f"{num1} {Operation_symbol} {num} = {answer}")
        quest = input('Do you want to continue y or n ?')
        if quest == 'y':
            num1 = answer
        elif quest == 'n':
            should_continue = False
            newcalc = input('Do you want to start new calculation ? if yes type y or else n: ')
            if newcalc == 'y':
                calculator()
            else:
                print('Closed the calculator')
                break
        else:
            print('Invalid input')
            should_continue = False
            break

calculator() 
