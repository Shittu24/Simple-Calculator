def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x* y

def divide(x, y):
    return x/ y

print("Select operation -\n" \
    "1.Add\n" \
    "2.Subtract\n" \
    "3. Multiply\n" \
    "4.Divide\n" )

choice = input("Enter choice(1/2/3/4):" )


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if choice == "1":
    print(x, "+" ,y  "=",
          add(x,y))

elif choice == "2":
    print(x, "-" ,y "=",
          subtract(x,y))

elif choice == "3":
    print(x, "*" ,y "=",
          multiply(x,y))

elif choice == "4":
    print(x, "/" ,y "=",
          divide(x,y))
else:
    print("Invalid input")

          


'''
add()
subtract()
multiply()
divide()
'''
