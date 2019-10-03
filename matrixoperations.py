m=int(input("enter the no.of rows:"))
n=int(input("enter the no.of column:"))
a=[0]*m
for i in range(m):
	a[i]=[0]*n
b=[0]*m
for i in range(m):
	b[i]=[0]*n
c=[0]*m
for i in range(m):
	c[i]=[0]*n
d=[0]*m
for i in range(m):
	d[i]=[0]*n
print("enter matrix 1:")
for i in range(m):
	for j in range(n):
		a[i][j]=int(input())
print("enter the matrix 2:")
for i in range(m):
	for j in range(n):
		b[i][j]=int(input())
for i in range(m):
	for j in range(n):
		c[i][j]=a[i][j]+b[i][j]
print("addition of matrix 1 and matrix 2=")
for i in range(m):
	for j in range(n):
		print(c[i][j],end=" ")
	print()
for i in range(m):
	for j in range(n):
		d[i][j]=a[i][j]-b[i][j]
print("subtraction of matrix 1 and matrix 2=")
for i in range(m):
	for j in range(n):
		print(d[i][j],end=" ")
	print()
