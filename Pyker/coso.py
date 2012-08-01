f = open('fick.song','r')
a = []
b = []
t = ''
N = 0
for c in f.read():
	if c == ' ':
		a += [t]
		t = ''
		continue
	if c == "\n":
		b += [t]
		t = ''
		N += 1
	t += c
print a
print b
