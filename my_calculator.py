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
    result = my_operation * my_second_operation
    return result


# my_list = ["12", "x", "(", "2", "+", "(", "2", "x", "(", "4", "+", "8", ")", ")", ")", "="]
# my_list = ["2", "+", "3", "x", "4", "+" ,"(", "1", "+", "(", "3", "+", "4", ")", ")", "="]
    
user_truc = ""  
my_list = []
operator = ["+", "-", "x", ":","(",")"]        

while user_truc != "=":
    user_truc = input("entrez des trucs")
    if user_truc == "=":
        break
    if user_truc in operator or user_truc.isdigit():
        my_list.append(user_truc)  
    else:
        print(f"Erreur : '{user_truc}' n'est pas accepté.")

# quand il y a les parenthèses il fo absolument un signe avant la première parenthèse (
# et un signe après la parenthèse 

# print(my_list)
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
    # print(my_list)
    last = 0
    my_stuff = []
    index = 0
    while index < len(my_list):
        if my_list[index] == "(":
            # print(my_list[index])
            # print(index)
            while my_list[index] != ")":
                counterp = my_list.count("(")
                if my_list[index] == "(":
                    last = index
                index +=1
            index +=1
        else : index +=1
    # print(counterp)
    index = last +1
    # print(my_list[index])
    while my_list[index] != ")":
        my_stuff.append(my_list[index])
        index +=1
    truc(my_stuff)
    # print(my_stuff)
    index2 = last +1
    my_list[last] = my_stuff[0]
    # print(my_list)
    while my_list[index2] != ")":
        del my_list[index2]
    del my_list[index2]
    # print(my_list)
    if counterp == 1:
        truc(my_list)


index = 0
while index < len(my_list):
    # print(index)
    if my_list[index] == "(":
        index +=1
        while index < len(my_list):
            # print("truc", index)
            parenthesis(my_list)
            index +=1
    else : index +=1
# print(len(my_list))
truc(my_list)
# print(my_list)
# del my_list[-1]
print(my_list[0])
