
#n+nn+nnn

number=input("Enter a Number n : ")
sum_str='0'
sums=0
for i in range(3):
    sum_str=sum_str+number
    sums=sums+int(sum_str)
print("The Result is : ",sums)

#n+n*n+n*n*n

n = int(input("Enter n: "))
print(n+n*n+n*n*n)

