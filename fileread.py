from sys import argv

script, filename = argv

ab = open(filename)

print "your file is %s" %(filename) 
print ab.read()

print "Enter the file again"
ab1 = raw_input(">");

rd = open(ab1)
print "your second file %s" %(ab1)
print rd.read()

