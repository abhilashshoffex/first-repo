from sys import argv


script, ff, ft = argv

print "copying file from %s to %s " %(ff,ft)
f1 = open(ff)
rd = f1.read()

# checking existing file
print "the length is",len(rd)


#inserting to other file
f2 = open(ft, 'w')
f2.write(rd)

f1.close()
f2.close()
