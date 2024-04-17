
def function(num1):
    
    if num1 < 0:
        print("its negative number")
        
    elif num1 == 0:
        print("the factorial is 1:")
    else:
        fact = 1
        for i in range(1, num1+1):
            fact = fact*i
    print(fact) 
    return(num1)


num1 = int(input("Enter the number:"))
function(num1)           