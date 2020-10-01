
# funcions
def print_menu():
    print("-" * 20)
    print(" Python Calc")
    print("-" * 20)

    print("[1] Add")
    print("[2] Substract")
    print("[3] Multiply")
    print("[4] Division")

    print("[5] My age")

    print('[x] Close')


"""
opc = 5
ask for the year of birth
tell the age (+/- 1)
"""

# instructions
opc = ''
while( opc != 'x'):
    print_menu()
    opc = input('Please choose an option: ')
    
    if(opc != 'x'):
        num1 = input("First number: ")
        num2 = input("Second number: ")
    
    if(opc == '1'):    
        res = float(num1) + float(num2)
        print("Result " + str(res))

    elif (opc == '2'):
        res = float(num1) - float(num2)
        print("Result " + str(res))

    elif (opc == '3'):
        res = float(num1) * float(num2)
        print("Result " + str(res))

    elif(opc == '4'):
        # check if the num2 is 0
        # if so, show an error
        # else divide and show the result
        if(num2 == '0'):
            print("Don't dive by zero, U will kill us ALL")
        else:
            res = float(num1) / float(num2)
            print("Result: " + res)


print('Good bye!')
