HISTORY_FILE ="History.txt"

def show_history():
    file=open("HISTORY_FILE",'r')
    lines=file.readlines()
    if len(lines) ==0:
        print("History Not Found")
    else:
        for line in reversed(lines):         #from the last line to the first line.
            print(line.strip())
    file.close()

def clear_History():
    file=open("HISTORY_FILE",'w')
    file.close()
    print("History Cleared")

def Save_to_History(equation,result):
    file=open("HISTORY_FILE",'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def Calculate(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print("Invalid Input")
        return
    
    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])

    if op == "+" :
        result = num1 + num2
    elif op == "-" :
        result = num1 - num2
    elif op == "*" :
        result = num1 * num2
    elif op == "/" :
        if num2==0:
            print("Cannot divide by Zero")
            return
        result = num1 / num2
    else:
        print("Invalid Operator")
        return
    
    if int(result)==result:
        result = int(result)
    print("Result:",result)
    Save_to_History(user_input,result)

def main():
    print("SIMPLE CALCULATOR---------")
    while(True):
        user_input=input("Enter Calculation & command like history,exit,clear:")
        if user_input=='history':
            show_history()
        elif user_input=='clear':
            clear_History()
        elif user_input=='exit':
            print("GoodBye")
        else:
            Calculate(user_input)
main()


