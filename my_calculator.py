
result = 0

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

def truc(my_list):
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
    my_stuff = []
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
        my_stuff.append(my_list[index])
        index +=1
    truc(my_stuff)
    index2 = last +1
    my_list[last] = my_stuff[0]
    while my_list[index2] != ")":
        del my_list[index2]
    del my_list[index2]
    if counterp == 1:
        truc(my_list)

def menu():

    operator = ["+", "-", "x", ":","(",")"]        
    user_input = ""
    my_list = []
    index = 0

    while user_input != "=":
        user_input = input("Entrez un nombre ou un opérateur (+, -, x, : ou ())")
        if user_input == "=":
            break
        if user_input in operator or user_input.isdigit():
            my_list.append(user_input)
        else:
            print(f"Erreur : '{user_input}' n'est pas accepté.")
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
    truc(my_list)

    print(my_list[0])
    menu()
menu()

