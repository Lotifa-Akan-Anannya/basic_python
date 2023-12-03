N=int(input("enter the integer value: "))
flag=False
if N==1:
  print("Not Prime")
else:
  for i in range(2,N):
    if (N % 1)==0:
      flag=True
      break
  if flag:
   print("Not Prime")  
  else:
   print("Prime") 
