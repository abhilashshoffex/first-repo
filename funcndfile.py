from sys import argv

script, file_name = argv

def print_all(f):
 print f.read()

def rewind(f):
 print f.seek(0)

def print_line(ln_no, f):
 print "printing line by line"
 print ln_no, f.readline()

f1 = open(file_name)
print_all(f1)

rewind(f1)


cur_ln = 1
print_line(cur_ln, f1)

print_line(cur_ln+1, f1)

print_line(cur_ln+2, f1)
