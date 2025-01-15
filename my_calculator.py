# my_operation = ""
# my_number = ""

# for i in my_operation:
#     if ord(i) in range(48,57):
#         my_number += i
#     else : return "pas bon"

# user_answer = ""

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


my_list = []
user_truc = ""

while user_truc != "=":
    user_truc = input("entrez des trucs")
    my_list.append(user_truc)



print(my_list)
def truc(my_list):
    i = 0
    while i < len(my_list):
        parenthesis(my_list, i)
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

def parenthesis(my_list, index):
    my_stuff = []
    while index < len(my_list):
        if my_list[index] == "(":
            index +=1
            while my_list[index] != ")":
                my_stuff.append(my_list[index])
                index += 1
        index +=1
    print(my_stuff)
haha = parenthesis(my_list)
