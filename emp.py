#print("welcome to code ")
import random

def emp_attd():
    randnumber = random.random()
    threshold = 0.5
    if randnumber < threshold:
        print("absent")
        return 0
    else:
        print("present")
        return 1
emp_attd()