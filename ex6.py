# Declare string where 10 is replacint the formatted character
x = "There are %d types of people." % 10

# delclare variable binary the string binaary
binary = "binary"

# declare variable do_not the string don't
do_not = "don't"


y = "Those who know %s and those who %s." % (binary, do_not)

# print the string "There are 10 types of people."
print x

# print the string "Those who know binary and those who don't."
print y

# print the string "I said 'There are 10 types of people.'"
print "I said: %r." % x


# print the string "I also said: 'Those who know binary and those who don't.'."
print "I also said: '%s'." % y

# declaring boolean variable to be false
hilarious = False

# delaring joke_evaluation to a string
joke_evaluation = "Isn't that joke so funny?! %r"

# print the string "Isn't that joke so funny
print joke_evaluation % hilarious

# declare string to "w"
w = "This is the left side of..."

# declare sting to "e"
e = "a string with a right side."

# print the string "w" + "e"
print w + e
