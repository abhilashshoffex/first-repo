
class parent(object):
 def implicit(self):
  print "Parent implicit"

 def override(self):
  print "Parent override"
 
 def altered(self):
  print "Parent altered"

class child(object):
 def __init__(self):
   self.par = parent()

 def implicit(self):
  self.par.implicit()
 
 def altered(self):
  print "Before parent altered"
  self.par.altered()
  print "After parent altered"

 def override(self):
  print "Child override function"


son = child()

son.implicit()
son.altered()
son.override()
