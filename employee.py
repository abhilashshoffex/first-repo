from sys import argv
script, filename = argv

ab1 = open(filename, 'w')
  
ch = 0
print "Enter your choise"
while ch != 3:
 print "\n1)Add record\n2)Display record\n3)Exit "
 print "Enter your choice:-",
 ch = int(raw_input())
 if ch == 1:
  print "Enter the employee ID:",
  eid = raw_input()
  print "Enter the Employee name:",
  enm = raw_input()
  ab1.write(eid)
  ab1.write("\t")
  ab1.write(enm)
  ab1.write("\n")
  
 elif ch == 2:
  ab1.close()
  ab = open(filename)
  print ab.read()
 elif ch == 3:
  exit(0)

