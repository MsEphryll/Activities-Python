from multiprocessing import Process, Lock
from time import sleep
from random import random


def addNum(num1, num2, lock, pname):
  total = num1 + num2
  with lock:
    randomSleepTime = random() * 10
    print(f"<process name: {pname} got the lock. The sum of the numbers is {total}, sleeping for {randomSleepTime}")
    sleep(randomSleepTime)

def subtractNum(num1, num2, lock, pname):
  total = num1 - num2
  with lock:
    randomSleepTime = random() * 10
    print(f"<process name: {pname} got the lock. The difference of the numbers is {total}, sleeping for {randomSleepTime}")
    sleep(randomSleepTime)

def multiplyNum(num1, num2, lock, pname):
  total = num1 * num2
  with lock:
    randomSleepTime = random() * 10
    print(f"<process name: {pname} got the lock. The product of the numbers is {total}, sleeping for {randomSleepTime}")
    sleep(randomSleepTime)

def divideNum(num1, num2, lock, pname):
  total = num1 / num2
  with lock:
    randomSleepTime = random() * 10
    print(f"<process name: {pname} got the lock. The quotient of numbers is {total}, sleeping for {randomSleepTime}")
    sleep(randomSleepTime)

if __name__ == '__main__':

  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))

  lock = Lock()

  add_num = Process(target=addNum, args=(num1, num2, lock, "Add Number"))
  subtract_num = Process(target=subtractNum, args=(num1, num2, lock, "Subtract Number"))
  multiply_num =Process(target=multiplyNum, args=(num1, num2, lock, "Multiply Number"))
  divide_num = Process(target=divideNum, args=(num1, num2, lock, "Divide Number"))

  add_num.start()
  subtract_num.start()
  multiply_num.start()
  divide_num.start()

  add_num.join()
  subtract_num.join()
  multiply_num.join()
  divide_num.join()