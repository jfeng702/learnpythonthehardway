# brings in argv module

print "Type the filename :"
# brings in filename argument
file_again = raw_input("> ")

# brings filename into memory and saves under txt
txt_again = open(file_again)

# Reads filename
# print "Here's your file %r:" % txt
# print txt.read()

# # repeats the open and read
# print "Type the filename again:"
# file_again = raw_input("> ")
#

#
print "Here's your file %r:" % file_again
print txt_again.read()
close(txt)
close(txt_again)
