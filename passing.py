from sys import argv

script, user_name = argv
prompt='>'

print "hi %s, I' m the % s script." %(user_name,script)
print "I'd like to ask you a few quetions."
print "Do like me %s?" %user_name
likes = raw_input(prompt)

print "Where do u live %s?" %user_name
lives = raw_input(prompt)

print "what kind of computer do u have?"
computer = raw_input(prompt)

print """
Alright, so u said %r about liking me.
U live in %r. Not sure where that is.
And you have a %r computer. nice.
""" %(likes,lives,computer)
