def calcule(num1,operator,num2):
    if operator == "*": 
        return num1*num2
    elif operator == "/":
        return num1/num2
    elif operator =="+":
        return num1+num2
    elif operator == "-":
        return num1-num2 
print(calcule(7,"*",7))
print(calcule(12,"+",12)) 
print(calcule(45,"/",45))
print(calcule(50,"-",25))   
