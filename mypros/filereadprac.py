		# importing the argv from system
		#sys is package and argv is feature from that package
from sys import argv
		#store the 2 variables in argv
script, filename = argv
		#the above line take the file name, so openning that file name in variable
file1 = open(filename)
		# printing your file
print "your file is %s " %(filename)
		#printing the file contents
print file1.read()
	
		#taking other file as input in file2 variable
print "Enter the another file name"
file2 = raw_input(">>>");

		#opening that file 
rd = open(file2)
		# printing another file
print "your another file is %s" %(file2)
		#printing the file2 contents
print rd.read()
