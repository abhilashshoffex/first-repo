from sys import argv

script, ff, ft = argv

print "file will copy from %s to %s" %(ff,ft)

f1 = open(ff)
rd = f1.read()

print "file is copying..."
f2 = open(ft, 'w')
f2.write(rd)

f1.close()
f2.close()

