num = int(input("enter the number of rows"))
for i in range(1,num):
  for j in range(1,-i,-1):
    print(end=" ")
  for j in range (0,i+1):
    print("*",end=" ")
  print()
