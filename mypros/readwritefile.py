from sys import argv

script, filename = argv

print "i am openning the %s file" %(filename)
f1 = open(filename, 'w')

print "i am erasing that file "
print "press ctrl+c to abort"
print "enter to continue"

raw_input("?")

print "file is erased"

print "enter any 3 lines to write in that file"
s1 = raw_input("line1:")
s2 = raw_input("line2:")
s3 = raw_input("line3:")

print "i am inserting this lines in that file"
f1.write(s1)
f1.write("\n")
f1.write(s2)
f1.write("\n")
f1.write(s3)

print "file operation is finished"
f1.close()
