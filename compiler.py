import sys, os, tempfile
gs="ruby golfscript.rb"
def ns(n):
	l=0
	while n>=256**l:
		n-=256**l
		l+=1
	return "".join(chr(n/(256**i)%256) for i in range(l-1,-1,-1))

code = ns(long(sys.argv[1].split('.')[-2]))
print(code)
os.system("%s %s"% (gs, code))