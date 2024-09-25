print("""\nWhat would you like to do?
  - (A)dd
  - (S)ubtract
  - (M)ultiply
  - (D)ivide
  - (Q)uit
""")

op = input().upper()

if op == "A":
  num1 = float(input("Please enter the first number: "))
  
  num2 = float(input("""\nPlease enter the second number: """))
  ans = str(num1 + num2)
  num1 = str(num1)
  num2 = str(num2)

  print("""\nAdding """ + num1 + " and " + num2 + " gives you the result of " + ans)
  
elif op == "S":
  num1 = float(input("Please enter the first number: "))
  num2 = float(input("Please enter the second number: "))
  ans = str(num1 - num2)
  num1 = str(num1)
  num2 = str(num2)

  print("\nSubtracting " + num1 + " and " + num2 + " gives you the result of " + ans)

elif op == "M":
  num1 = float(input("Please enter the first number: "))
  num2 = float(input("Please enter the second number: "))
  ans = str(num1 * num2)
  num1 = str(num1)
  num2 = str(num2)

  print("\nMultiplying " + num1 + " and " + num2 + " gives you the result of " + ans)

elif op == "D":
  num1 = float(input("Please enter the first number: "))
  num2 = float(input("Please enter the second number: "))
  ans = str(num1 / num2)
  num1 = str(num1)
  num2 = str(num2)

  print("\nDividing " + num1 + " and " + num2 + " gives you the result of " + ans)

elif op == "Q":
  print("""
Goodbye!""")
else:
  print("""
Goodbye!""")
