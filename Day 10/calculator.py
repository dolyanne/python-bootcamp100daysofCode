def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations_dict = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
num1 = int(input("what is the first number? : "))
num2 = int(input("what is the second number?: "))
for symbol in operations_dict:
  print(symbol)
operation_symbol = input("Pick an operations symbol: ")
cal_function = operations_dict[operation_symbol]
answer =cal_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
