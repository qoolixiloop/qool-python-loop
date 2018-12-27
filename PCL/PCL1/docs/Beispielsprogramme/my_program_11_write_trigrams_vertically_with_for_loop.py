# Python program to write letter trigrams
# by Martin Volk

# initialize the variable
#text = 'programmieren macht spass'
text = '01234567'

# while the position is smaller than the length of the text
for position in range(3, len(text)+1):
	# print the trigram
	print position, ": ",text[position-3:position]
print "position", len(text)+1, "wird im range nicht angenommen.\n" \
				+"(Bis aber nicht inklusive)"
