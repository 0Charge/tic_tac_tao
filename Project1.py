from termcolor import colored,cprint
from colorama import Fore
def f(y):
	for i in range(7):
		if i%2==0:
			for j in range(7):
				p=int(i/2)
				q=int(j/2)
				if j%2==0:
					if y[q][p]!=" ":
						cprint(y[q][p],end="")
					else:
						print(" ",end="")
				else:
					print(colored("|",'green'),end="")

		else:
			print(" ")
			print(colored("-------",'green'))
	print(" ")
			
x=[[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
player=1
f(x)
print(" ")
a=0
a2=0
a1=0
b1=0
b=0
c=0
d=0
while True:
	print("player",player)
	try:
		k=int(input("colum:"))
	except ValueError:
		print("enter valied input")
		if player==1:
			player=1
			continue
		else:
			player=2
			continue
	if k>4:
		print("wrong input please re-enter")
		continue
	l=3
	while l>=0:
		if player==1:
			if x[k-1][l]==" ":
				a=(f'{Fore.RED}'+u'\u2713')
				I=l
				a1=a1+1
				player=2
				break
			else:
				if l==0:
					print("full colum")
					player=1
					break			
		else:
				if x[k-1][l]==" ":
					a=(f'{Fore.CYAN}'+u'\u2613')
					I=l
					b1=b1+1
					player=1
					break
				else:
					if l==0:
						print("full colum")
						player=2
						break
		l-=1
	x[k-1][I]=a
	f(x)
	for R in range(4):
		c1=0
		c2=0
		for C in range(4):
			if x[R][C]==(f'{Fore.RED}'+u'\u2713'):
				c1=c1+1
				b=c1
				if c1==4:
					print("player1 wins")
					break
			if x[R][C]==(f'{Fore.CYAN}'+u'\u2613'):
					c2=c2+1
					b=c2
					if c2==4:
						print("player2 wins")
						break
		if b==4:
			break
	S=0
	c3=0
	c4=0
	while S<4:
			if x[S][S]==(f'{Fore.RED}'+u'\u2713'):
				c3=c3+1
				c=c3
				if c3==4:
					print("player1 wins")
					break
			if x[S][S]==(f'{Fore.CYAN}'+u'\u2613'):
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
		if x[P][Q]==(f'{Fore.RED}'+u'\u2713'):
			c5=c5+1
			d=c5
			if c5==4:
				print("player1 wins")
				break
		if x[P][Q]==(f'{Fore.CYAN}'+u'\u2613'):
			c6=c6+1
			d=c6
			if c6==4:
				print("player2 wins")
				break
		P+=1
		Q-=1
			
	if b==4 or c==4 or d==4:
		break
	if a1==8 and b1==8:
		print("no one wins")
		break												
	print(" ")
				
			
		
		