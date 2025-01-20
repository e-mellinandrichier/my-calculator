
result = 0

histo =[]
def load_history():
    try:
        with open("histo.txt", "r") as file:
            global histo
            histo = file.readlines()
    except FileNotFoundError:
        pass
def save_history():
    with open("histo.txt", "w") as file:
        for element in histo:
            file.write(element + "\n")
def display_histo():
    if not histo:
        print("History is empty.")
    for element in histo:
        print(element)
def supr_histo():
    supr = input("Do you want to delete history? (YES/NO) : ")
    if supr == "YES":
        histo.clear()
        save_history()
        print("History has been deleted")
        menu()
    elif supr == "NO":
        menu()

def add(my_operation, my_second_operation):
    result = my_operation + my_second_operation
    return result

def minus(my_operation, my_second_operation):
    result = my_operation - my_second_operation
    return result

def multiply(my_operation, my_second_operation):
    result = my_operation * my_second_operation
    return result

def division(my_operation, my_second_operation):
    result = my_operation * my_second_operation
    return result

def calculator(my_list):
    i = 0
    while i < len(my_list):
        if my_list[i] == "x" or my_list[i] == ":":
            if my_list[i] == "x":
                result = multiply(float(my_list[i-1]), float(my_list[i+1]))
                del my_list[i+1]
                my_list[i] = result
                del my_list[i-1]
                i-=1
            if my_list[i] == ":": 
                if int(my_list[i-1]) == 0 or int(my_list[i +1]) == 0: 
                    print("Division par 0 impossible, veuillez recommencer.")
                    menu()
                result = division(float(my_list[i-1]), float(my_list[i+1]))
                del my_list[i+1]
                my_list[i] = result
                del my_list[i-1]
                i -=1
        i +=1
    i = 0
    while i < len(my_list):
        if my_list[i] == "+":
            result = add(float(my_list[i-1]), float(my_list[i+1]))
            del my_list[i+1]
            my_list[i] = result
            del my_list[i-1]
            i -= 1
        if my_list[i] == "-":
            result = minus(float(my_list[i-1]), float(my_list[i+1]))
            del my_list[i+1]
            my_list[i] = result
            del my_list[i-1]
            i -=1
        i +=1
    return(my_list)

def parenthesis(my_list):
    last = 0
    my_list2 = []
    index = 0
    while index < len(my_list):
        if my_list[index] == "(":
            while my_list[index] != ")":
                counterp = my_list.count("(")
                if my_list[index] == "(":
                    last = index
                index +=1
            index +=1
        else : index +=1
    index = last +1
    while my_list[index] != ")":
        my_list2.append(my_list[index])
        index +=1
    calculator(my_list2)
    index2 = last +1
    my_list[last] = my_list2[0]
    while my_list[index2] != ")":
        del my_list[index2]
    del my_list[index2]

def menu():

    operator = ["+", "-", "x", ":","(",")"]        
    user_input = ""
    my_list = []
    index = 0
    jindex = 0
    operatorparam = ["+", "-", ":", "x"]
    operatorparam2 = ["+", "-", ":", "x", "("]
    parenthesisparam = ["(", ")"]

    while user_input != "=":
        user_input = input("__________Enter a number or an operator sign (+, -, x, : ou ())__________\n")
        if user_input == "=":
            break
        if user_input in operator or user_input.lstrip("-").isdigit():
            my_list.append(user_input)
            while jindex < len(my_list):
                if jindex == 0:
                    if my_list[jindex] in operatorparam or my_list[jindex] == ")":
                        print("Not valid. Please try again")
                        menu()
                if jindex >= 1:
                    if my_list[jindex].lstrip("-").isdigit():
                        if my_list[jindex - 1] not in operator:
                            print("Not valid. Please try again")
                            menu()
                    if my_list[jindex] in operatorparam:
                        if my_list[jindex - 1] in operatorparam2:
                            print("Not valid. Please try again")
                            menu()
                    if my_list[jindex] == "(":
                        if my_list[jindex - 1] not in operatorparam:
                            print("Not valid. Please try again")
                            menu()
                    if my_list[jindex] == ")":
                        if my_list[jindex - 1] in operator:
                            print("Not valid. Please try again")
                            menu()

                    
                jindex +=1
        else:
            print(f"Error : '{user_input}' is not valid.")
    operation = ""
    for e in my_list:
        operation += e
    print(operation, "=")

    index = 0
    while index < len(my_list):
        if my_list[index] == "(":
            index +=1
            while index < len(my_list):
                parenthesis(my_list)
                index +=1
        else : index +=1
    calculator(my_list)
    print(my_list[0])
    histo.append(f"{operation} = {my_list[0]}")
    view_histo = input("Write (view) to display history:")
    if view_histo=="view":
        try:
            display_histo()
            supr_histo()
        except:
            print("Please enter a correct input")
            menu()
    save_history()
    menu()
load_history()
menu()

