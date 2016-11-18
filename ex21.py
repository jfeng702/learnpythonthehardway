def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# what = add(age, multiply(height, multiply(weight, divide(iq, 2))))
what = multiply(height, subtract(weight, age))

print "That becomes: ", what, "Can you do it by hand?"

print "What is number 1?"
num1 = int(raw_input("> "))
print "What is number 2?"
num2 = int(raw_input("> "))
add(num1, num2)
print "Age: %d" % (num1 + num2)
what2 = subtract(add(24,divide(34, 100)),1023)
print "That becomes: ", what2


# def add(a, b):
#     print "ADDING %d + %d" % (a, b)
#     return a + b
#
# age = add(5, 3)
# print "Age: %d" % age
