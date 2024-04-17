#Q.4Write a Python function to find the maximum of three numbers.


def find_max(num1,num2,num3):
    
    
  largest = num1 if num1 >= num2 else num2

  
  return largest if largest >= num3 else num3
    
    
max_value = find_max(10, 20, 5)

#  num1 = int(input("Enter first number:"))
#  num2 = int(input("Enter first number:"))
#  num3 = int(input("Enter first number:"))
print(f"The maximum value is = {max_value}")

     

  