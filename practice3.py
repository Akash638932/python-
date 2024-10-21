#q1 wap to check if a number entered by the user is odd or even.
num=int(input("enter the number:"))
rem=num%2
if(rem==0):
    print("even")
else:
    print("odd")

#q2 wap to find the greatest of 3 number entered by the user.
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a>=b and a>=c):
    print("first number is largest",a)
elif(b>=c):
    print('second number is largest',b)
else:
    print("third is largest",c)


#q3 wap to check if a number is a multiple of 7 or not.
x=int(input("enter the number:"))
if(x% 7==0):
    print("multiple of 7")
else:
    print("not a multiple")
    