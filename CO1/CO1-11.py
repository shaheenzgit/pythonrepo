num1=int(input("Enter Number 1 : "))
num2=int(input("Enter Number 2 : "))
num3=int(input("Enter Number 3 : "))
if((num1>=num2)&(num1>=num3)):
    print("The Biggest Number is : ",num1)
elif((num2>=num1)&(num2>=num3)):
    print("The Biggest Number is : ",num2)
else:
    print("The Biggest Number is : ",num3)
