import sys, os, tempfile
gs="./golfscript.rb"
def ns(n):
	l=0
	while n>=256**l:
		n-=256**l
		l+=1
	return "".join(chr(n/(256**i)%256) for i in range(l-1,-1,-1))
print(sys.argv)
p = sys.argv[0]
if os.stat(p).st_size == 0:
	tmp = tempfile.NamedTemporaryFile()
	tmp.write(ns(long(sys.argv[0].split('.')[-2])))		# Script name = meta-gs.N.py
	tmp.flush()
	p = tmp.name
print(gs)
print(p)
os.system("%s %s"% (gs, p))