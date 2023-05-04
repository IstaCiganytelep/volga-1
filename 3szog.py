#haromszog
a=int(input("Add meg a háromszög 'a' oldalát"))
b=int(input("Add meg a háromszög 'b' oldalát"))
c=int(input("Add meg a háromszög 'c' oldalát"))

if c<a and a<b+c and b<a+c:
	print ("a(z)",a,",",b,",",c,"3szögetalkot")
else:
	print ("a(z)",a,",",b,",",c," 3szöge nem talkot")
	
