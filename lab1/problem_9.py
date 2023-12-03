str=input("Enter the string: ")
N=int(input("Enter the integer: "))

str1=""
for i in range(N,len(str)):
  str1=str1+str[i]
  print("New String: ",str1)
