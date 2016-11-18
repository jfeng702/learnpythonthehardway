
numbers = []

def while_loop(end, step):
    for i in range(0,end):
        print "At the top i is %d" % i
        numbers.append(i)

        # i += step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    # i = 0
    #
    # while i < a:
    #     print "At the top i is %d" % i
    #     numbers.append(i)
    #
    #     i += b
    #     print "Numbers now: ", numbers
    #     print "At the bottom i is %d" % i




while_loop(10,2)

print "The numbers: "

for num in numbers:
    print num
