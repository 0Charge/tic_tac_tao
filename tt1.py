def f(x):
	for i in range(7):
				if i%2==0:
					pi=int(i/2)
					for j in range(7):
						pj=int(j/2)
						if j%2==0:
							print(x[pj][pi],end="")			
						else:
							print("|",end="")
				else:
					print(" ")
					print("-------")
	print(" ")
							
player=1 
co=[[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
f(co)
print(" ")
a=0
b=0
c=0
d=0
a1=0
b1=0
while True:
	print("player:",player)
	k=int(input("colum:"))
	r=int(input("row:"))
	if r>4 or k>4:
		print("wrong input pls re-enter")
		continue
	if player==1:
		if co[k-1][r-1]==" ":
			co[k-1][r-1] = "X"
			a1=a1+1
			player=2
	else:
		if co[k-1][r-1]==" ":
			co[k-1][r-1] ="O"
			b1=b1+1
			player=1
	f(co)
	for R in range(4):
		c1=0
		c2=0
		for C in range(4):
			if co[R][C]=="X":
				c1=c1+1
				a=c1
				if c1==4:
					print("player1 wins")
					break
			if co[R][C]=="O":
					c2=c2+1
					a=c2
					if c2==4:
						print("player2 wins")
						break
		if a==4:
			break
	S=0
	c3=0
	c4=0
	while S<4:
			if co[S][S]=="X":
				c3=c3+1
				c=c3
				if c3==4:
					print("player1 wins")
					break
			if co[S][S]=="O":
				c4=c4+1
				c=c4
				if c4==4:
					print("player2 wins")
					break
			S+=1
			
	P=0
	Q=3
	c5=0
	c6=0
	while P<4 and Q>=0:
		if co[P][Q]=="X":
			c5=c5+1
			d=c5
			if c5==4:
				print("player1 wins")
				break
		if co[P][Q]=="O":
			c6=c6+1
			d=c6
			if c6==4:
				print("player2 wins")
				break
		P+=1
		Q-=1
			
	if a ==4 or b==4 or c==4 or d==4:
		break
	if a1==8 and b1==8:
		print("no one wins")
		break												
	print(" ")
		
		