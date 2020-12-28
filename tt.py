def f(x):
	for i in range(7):
				if i%2==0:
					pi=int(i/2)
					for j in range(7):
						pj=int(j/2)
						if j%2==0:
							print(x[pi][pj],end="")
						else:
							print("|",end="")
				else:
					print(" ")
					print("-------")		
player=1 
co=[[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
f(co)
print(" ")
while True:
	print("player:",player)
	c=int(input("colum:"))
	r=int(input("row:"))
	if player==1:
		if co[r-1][c-1]==" ":
			co[r-1][c-1] = "X"
			player=2
	elif co[r-1][c-1]==" ":
		co[r-1][c-1] ="O"
		player=1
	f(co)
	print(" ")
		
		