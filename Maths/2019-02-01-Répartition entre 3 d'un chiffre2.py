x=int(input("x="))
m=int(input("m="))
A=min(x,m)
B=min(x-A,m)
C=min(x-(A+B),m)
print("A=",A,";B=",B,";C=",C)
