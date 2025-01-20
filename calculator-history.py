


histo = []

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
        print("Historique vide.")
    for element in histo:
        print(element)

def supr_histo():
    supr = input("Do you want to delete history? (YES/NO) : ")
    if supr == "YES":
        histo.clear()
        save_history()
        print("History has been deleted")
        Calculator()
    elif supr == "NO":
        Calculator()

def Calculator():
    user_input = input("Write (history) to display historic or Enter your calcul: ")
    if user_input == "history":
        try:
            display_histo()
            supr_histo()
        except:
            print("Please enter a correct input")
            Calculator()
    else:
        try:
            a, o, b = user_input.split()
            a = float(a)
            b = float(b)

            if o == "+":
                result = a + b
            elif o == "-":
                result = a - b
            elif o == "*":
                result = a * b
            elif o == "/":
                if b == 0:
                    print("Impossible to divide by 0")
                    Calculator()
                else:
                    result = a / b
            else:
                print("Invalid operator")
                Calculator()

            histo.append(f"{a} {o} {b} = {result}")
            save_history() 
            print(result)
            Calculator()

        except ValueError:
            print("Invalid input")
            Calculator()

load_history()
Calculator()
    







