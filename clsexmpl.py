class song(object):

 def _init_(self, lyrics):
  self.lyrics = lyrics
 
 def sing(self):
  for line in self.lyrics:
   print line

hbd = song(["Hbd to u",
	     "i dont want to eat",
             "so i will stop u"])

bull = song(["Hjd ldf lfnied",
	     "kjds jf jfiefi ifk",
             "jdkf ijefi ikeni iken"])

hbd.sing()
bull.sing()
