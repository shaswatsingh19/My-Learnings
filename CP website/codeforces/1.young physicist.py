m = int(input("Enter the number of rows"))
mat =[]
for i in range(0,m):
        mat.append([])
        
for i in range(0,m):
        for j in range(0,3):
            mat[i].append(j)
            mat[i][j] = int(input())

sum = 0

for i in range(0,m):
    sum = sum + mat[i][1] +  mat[i][2] + mat[i][0]
    
if (sum)==0: 
    print("yes")
else:
    print("No")
