def ns(n):
	l=0
	while n>=256**l:
		n-=256**l
		l+=1
	return "".join(chr(n/(256**i)%256) for i in range(l-1,-1,-1))
golf_num = "209180605381204854470575573749277224"

split = [golf_num[i:i+3] for i in range(0, len(golf_num), 3)]
string = ""
for char_code in split:
    char = chr(int(char_code))
    string += char

print(string)