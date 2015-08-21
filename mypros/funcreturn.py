def add(a, b):
 print "Addition of %d and %d" %(a, b)
 return a + b

def sub(a, b):
 print "Substraction of %d and %d" %(a, b)
 return a - b

def mul(a, b):
 print "multiplication of %d and %d " %(a, b)
 return a * b

def div(a, b):
 print "Division of %d and %d" %(a, b)
 return a / b

age = add(10, 20)
rank = sub(20, 10)
hieght = mul(2, 3)
w = div(100, 2)

print "age is %d and rank is %d" %(age, rank)

what = add(age, sub(rank, mul(hieght, div(w, 2))))
print "what", what

