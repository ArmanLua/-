a = input()
b = input()
c = ['','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX']
if a and b in c:
	a = c.index(a)
	b = c.index(b)
	n = a + b
	print( c[n] )
	



