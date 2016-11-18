# imports arguments
from sys import argv
# uses two arguments?
script, input_file = argv
# reads the argument "f"
def print_all(f):
    print f.read()
# rewind ?
def rewind(f):
    f.seek(0)
# readline returns stuff until a "\n" character is found"
def print_a_line(line_count, f):
    print line_count, f.readline(),
# input_file = argument from above
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
