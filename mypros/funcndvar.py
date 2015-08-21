# defining a function 
def cheese_and_cracker(chz, crkr):
 print "amount of cheese is %d and amount of cracker is %d" %(chz, crkr)

#calling the function
cheese_and_cracker(10,20)
print "or we can define it by using script variables"
chz1 = 30
crkr1 = 40

#passing the variables(which contains some value) to functions
cheese_and_cracker(chz1, crkr1)
print "we can do thi by adding math in this"
#doing math operation in function and passing the result
cheese_and_cracker(12+12, 30+12)

print "or we can use variable inside it"
#doing math operation with the variable
cheese_and_cracker(chz1+222, crkr1+10101)
