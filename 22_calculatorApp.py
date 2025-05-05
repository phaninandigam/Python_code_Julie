from art import logo
print(logo)


def add(n1, n2):
    return(n1 + n2)

def substract(n1, n2):
    return(n1 - n2)

def multiply(n1, n2):
    return(n1 * n2)

def divide(n1, n2):
    return(n1 / n2)

operators={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}
new_calculation = True
answer = 0
while new_calculation == True:
    n1 = int(input("whats' your first number?: "))
    for symbol in operators:
        print(symbol)
    should_continue = True
    while should_continue:

        operator = input("Pick an operation: ")
        n2 = int(input("whats' the next number?: "))
        function = operators[operator]
        answer=function(n1,n2)
        print(f"{n1} {operator} {n2}= {answer}")

        procced_calucaltion = input(
            f"Type 'y' to continue caluclating  with  {answer}, or type 'n' to start a new caluclation: ").lower()

        if procced_calucaltion == 'n':
            should_continue = False
        else:
            n1 = answer



