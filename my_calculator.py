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
    result = my_operation / my_second_operation
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
                result =division(float(my_list[i-1]), float(my_list[i+1]))
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
    user_truc = ""
    my_list = []
    index = 0

    while user_truc != "=":
        user_truc = input("Entrez un nombre ou un opérateur (+, -, x, : ou ())")
        my_list.append(user_truc)
    
    my_history_list = my_list

    index = 0
    while index < len(my_list):
        if my_list[index] == "(":
            index +=1
            while index < len(my_list):
                parenthesis(my_list)
                index +=1
        else : index +=1
    truc(my_list)
    del my_list[-1]
    print(my_list[0])
    menu()
menu()