# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print "You have %d cheeses!" % cheese_count
#     print "You have %d boxes of crackers!" % boxes_of_crackers
#     print "Man that's enough for a party!"
#     print "Get a blanket.\n"
#
# print "We can just give the function numbers directly:"
# cheese_and_crackers(20, 30)
#
# print "OR, we can use variables from our script:"
# amount_of_cheese = 10
# amount_of_crackers = 50
#
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
# print "We can even do math inside too:"
# cheese_and_crackers(10 + 20, 5 + 6)
#
# print "And we can combine the two, variables and math:"
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def gin_and_juice(gin_amt, juice_amt):
    print "You have %d L of gin and %d L of juice" % (gin_amt, juice_amt)

gin_and_juice(5, 10)

amount_of_gin = 10
amount_of_juice = 100

gin_and_juice(amount_of_gin + 1000, amount_of_juice - 1000)

print "How much gin? "
g_amt = raw_input("> ")
print "How much juice? "
j_amt = raw_input("> ")

gin_and_juice(int(g_amt), int(j_amt))
