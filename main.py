import art
print(art.logo)



def calculator(num1,num2,operation):
  if operation == "+":
    return num1+num2
  
  if operation == "-":
    return num1-num2
  
  if operation == "*":
    return num1*num2
  
  if operation == "/":
    return num1/num2

def operation():
  """choose operator"""
  operation = input(" \n + \n - \n * \n / \n Choose an operation : ")
  return operation

def begin():
  num1 = float(input("Whats the first number: "))

  operator = operation() 

  num2 = float(input("Whats the second number: "))

  result = calculator(num1,num2,operator)
  print(f"The answer is {result}")

  continue_f = input("Want to continue the operation on the result")

  while (continue_f == "y"):
    operator = operation() 
    num3 = float(input("Whats the second number: "))
    result = calculator(result,num3,operator)
    
    print(f"The answer is {result}")

    continue_f = input("Want to continue the operation on the result")
  again = input("Want to do a new calculation")
  return(again)
  

again = begin()
while (again =="y"):
  again = begin()
print("Goodbye, Have a nice day")
