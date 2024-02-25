import threading

def addNum(num1, num2):
  total = num1 + num2
  print(f"Sum of numbers: {total}")

def subtractNum(num1, num2):
  total = num1 - num2
  print(f"Difference of numbers: {total}")

def multiplyNum(num1, num2):
  total = num1 * num2
  print(f"Product of numbers: {total}")

def divideNum(num1, num2):
  total = num1 / num2
  print(f"Quotient of numbers: {total}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

threading.Thread(target=addNum, args=(num1, num2)).start()
threading.Thread(target=subtractNum, args=(num1, num2)).start()
threading.Thread(target=multiplyNum, args=(num1, num2)).start()
threading.Thread(target=divideNum, args=(num1, num2)).start()

print(" ")