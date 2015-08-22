class parent(object):
 def altered(self):
  print "Parent altered()"

class child(parent):
 def altered(self):
  print "Child before parent altered()"
  super(child, self).altered()
  print "CHild after parent altered()"

dad = parent()
son = child()

dad.altered()
son.altered() 
