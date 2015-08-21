print "Enter the first number:-",
num1 = int(raw_input())

print "Enter the second number:-",
num2 = int(raw_input())

print "Enter the third number:-",
num3 = int(raw_input())

if num1 > num2 and num1 > num3:
 print "First number is greater" 
elif num2 > num3:
 print "Second number is greater"
else:
 print "third number is greater"
