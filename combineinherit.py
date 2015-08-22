class parent(object):
 def override(self):
  print "Parent override"

 def altered(self):
  print "Parent altered"

 def implicit(self):
  print "Parent implicit"

class child(parent):
 def override(self):
  print "child override"

 def altered(self):
  print "Parent before altered"
  super(child, self).altered()

dad = parent()
son = child()

dad.override()
son.override()

dad.altered()
son.altered()

dad.implicit()
son.implicit()
