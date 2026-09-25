employeeDiction = {}

def show():
    print("list of employees: ")
    print(employeeDiction)

def add():
    name = input("enter name of employee: ")
    basicPay= int(input("enter basic pay: "))
    allowance=int(input("enter allowance: "))
    deductions=int(input("enter deductions: "))
    taxes=int(input("enter taxes: "))
    grossPay=basicPay+allowance
    netPay=grossPay-deductions-taxes

    employeeDiction.update({name:
                                {
                                    "basic pay":basicPay,
                                    "allowance":allowance,
                                    "deductions":deductions,
                                    "taxes":taxes,
                                    "gross pay":grossPay,
                                    "net pay":netPay
                                }
                            })

    print("employee details added: ")
    print(employeeDiction[name])

def remove():
    print("enter the name of the person to delete")
    deathNote=input()
    del employeeDiction[deathNote]

    print("deletion successful")

def modify():
    print("enter the name of the person to modify")
    inputName=input()
    print("which part of the profile do you want to modify")
    choice = int(input("1=name, 2=basic pay, 3=allowance, 4=deductions, and 5=taxes."))

    if choice==1:
        newName=input("enter the new name of the person: ")

        name= newName
        basicPay = employeeDiction[inputName]["basic pay"]
        allowance = employeeDiction[inputName]["allowance"]
        deductions = employeeDiction[inputName]["deductions"]
        taxes = employeeDiction[inputName]["taxes"]
        grossPay = basicPay + allowance
        netPay = grossPay - deductions - taxes

        employeeDiction.update({name:
            {
                "basic pay": basicPay,
                "allowance": allowance,
                "deductions": deductions,
                "taxes": taxes,
                "gross pay": grossPay,
                "net pay": netPay
            }
        })

        del (employeeDiction[inputName])

    elif choice==2:
        newPay=int(input("enter the new basic pay: "))

        name = employeeDiction[inputName]["name"]
        basicPay = newPay
        allowance = employeeDiction[inputName]["allowance"]
        deductions = employeeDiction[inputName]["deductions"]
        taxes = employeeDiction[inputName]["taxes"]
        grossPay = basicPay + allowance
        netPay = grossPay - deductions - taxes

        del (employeeDiction[inputName])

        employeeDiction.update({name:
            {
                "basic pay": basicPay,
                "allowance": allowance,
                "deductions": deductions,
                "taxes": taxes,
                "gross pay": grossPay,
                "net pay": netPay
            }
        })

    elif choice==3:
        newAllowance=int(input("enter the new allowance: "))

        name = employeeDiction[inputName]["name"]
        basicPay = employeeDiction[inputName]["basic pay"]
        allowance = newAllowance
        deductions = employeeDiction[inputName]["deductions"]
        taxes = employeeDiction[inputName]["taxes"]
        grossPay = basicPay + allowance
        netPay = grossPay - deductions - taxes

        del (employeeDiction[inputName])

        employeeDiction.update({name:
            {
                "basic pay": basicPay,
                "allowance": allowance,
                "deductions": deductions,
                "taxes": taxes,
                "gross pay": grossPay,
                "net pay": netPay
            }
        })

    elif choice==4:
        newDeductions=int(input("enter the new deductions: "))

    name = employeeDiction[inputName]["name"]
    basicPay = employeeDiction[inputName]["basic pay"]
    allowance = employeeDiction[inputName]["allowance"]
    deductions = newDeductions
    taxes = employeeDiction[inputName]["taxes"]
    grossPay = basicPay + allowance
    netPay = grossPay - deductions - taxes

    del (employeeDiction[inputName])

    employeeDiction.update({name:
        {
            "basic pay": basicPay,
            "allowance": allowance,
            "deductions": deductions,
            "taxes": taxes,
            "gross pay": grossPay,
            "net pay": netPay
        }
    })

    elif choice==5:
        newTaxes=int(input("enter the new taxes: "))

        name = employeeDiction[inputName]["name"]
        basicPay = employeeDiction[inputName]["basic pay"]
        allowance = employeeDiction[inputName]["allowance"]
        deductions = employeeDiction[inputName]["deductions"]
        taxes = newTaxes
        grossPay = basicPay + allowance
        netPay = grossPay - deductions - taxes

        del (employeeDiction[inputName])

        employeeDiction.update({name:
            {
                "basic pay": basicPay,
                "allowance": allowance,
                "deductions": deductions,
                "taxes": taxes,
                "gross pay": grossPay,
                "net pay": netPay
            }
        })

    else:
        print("invalid input")

    print("")

while True:
    print("choose an operation")
    print("1=add, 2=delete, 3=modify, 4=show, and 5=exit")
    choice=int(input())

    if choice==1:
        add()
    elif  choice==2:
        remove()
    elif choice==3:
        modify()
    elif choice==4:
        show()
    elif choice==5:
        exit()
    else:
        print("invalid input")