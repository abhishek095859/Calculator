def add(num):
    return sum(num)
def sub(num):
    result = num[0]
    for i in num[1:]:
        result -= num
    return result
def mult(num):
    result =1
    for i in num:
        result*= num
    return result
def div(num):
    result = num[0]
    for num in num[1:]:
        result /= num
    return result
    
    
def main():
   
    operator=input("enter operator + - * /")
    num=[]
    while True:
        user=input("enter the values:")
        if user == "":
            break
        try:
            num.append(int(user))
        except ValueError:
            print("enter a valid number")
    
    
   

    if operator == "+":
        result = add(num)
    elif operator == "-":
        result= sub(num)
    elif operator == "*":
        result= mult(num)
    elif operator == "/":
        if num == 0:
            print("Error:Cannot divide by zero")
            return 
        result= div(num)
    else:
        print("choose the correct operator")
        return 
    print(result)
if __name__ == "__main__":
    main()
    
