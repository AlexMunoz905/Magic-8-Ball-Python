import random

ques = raw_input("Question?: ")
print ques
#Variables
one = "No"
two = "if you try hard"
three = "ERR | USER ERROR"
four = "Yes"
five = "No effort means NO"
six = "You must try to get the answer you want"
seven = "No, try again"
eight = "Im just a computer man"

number = random.choice([one, two, three, four, five, six, seven, eight])
print number
