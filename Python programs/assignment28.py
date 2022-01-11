r_a = int(input("Enter the Number of rows  for matrix A: " ))
c_a = int(input("Enter the Number of Columns for matrix A: "))
print("Enter the elements of Matrix A:")
matrix_a= [[int(input()) for i in range(c_a)] for i in range(r_a)]
print("First Matrix is: ")
for n in matrix_a:
    print(n)
c_b = int(input("Enter the Number of Columns for matrix B: "))
print("Enter the elements of Matrix B:")
matrix_b= [[int(input()) for i in range(c_b)] for i in range(c_a)]
for n in matrix_b:
    print(n)
result=[[0 for i in range(c_b)] for i in range(r_a)]
for i in range(len(matrix_a)):
    for j in range(len(matrix_b[0])):
        for k in range(len(matrix_b)):
            result [i][j]+=matrix_a[i][k]*matrix_b[k][j]
print("\nMatrix_a X Matrix_b is: ")
for r in result:
    print(r)