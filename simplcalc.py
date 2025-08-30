print("making a calculator")
input1 = int(input("what is the first number"))
input2 = int(input("what is the second number"))
symbol = input("pick an operator(+, -, *, /):")

if symbol == '+':
     result = input1 + input2
elif symbol == '-':
     result = input1 - input2
elif symbol == '*':
     result = input1 * input2
elif symbol == '/':
    if input2 != 0:
     result = input1 / input2
    else:
        result = "error: division by zero"
else:
    result = "bru wat is that"

print("result:", result)
