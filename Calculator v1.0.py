from math import pow
a = float(input("Enter the first number:"))
op = input("Input the operation:")
b = float(input("Enter the second number:"))
result = None
if op == "+":
    result = a+b
elif op == "/":
    result = a/b
elif op == "-":
    result = a-b
elif op == "*":
    result = a*b
elif op == "pow":
    result = pow(a,b)
print("Result: {:.2f}".format(result))
