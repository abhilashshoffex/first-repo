print "A littele poem"

poem = """
\t\t Starting the poem
blah
blah
blah
\t\t poem end :-)
"""
print "*"*10
print poem
print "*"*10

five = 10-2+3-6
print "this should be five",five

def operat(str_ptm):
 run = str_ptm + 1000
 jump = run + 10000
 cri = jump + 555555
 return run, jump, cri

run, jump, cri = operat(10)
print "run %d jump %d cri %d" %(run, jump, cri)

print "or ",operat(10) 
