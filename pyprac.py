from sys import argv

script, ff, ft = argv

print "file from %s to file %s" %(ff,ft)
print "file is copying ..."
f1 = open(ff)
rd = f1.read()
print "press enter to continue"
raw_input('>')
print "file content is",rd

f2 = open(ft, 'w')
f2.write(rd)
print "file copy complete"

f1.close()
f2.close()
