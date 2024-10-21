#.................................................using for & range()..............................................
#q1 print numbers from 1 to 100.
for i in range(1,101):
    print(i)

#q2 print numbers from 100 to 1.
for i in range(101,0,-1):
    print(i)


#q3 print the multiplication table of a number n.
n=int(input("enter number:"))
for i in range(1,11):
    print(n*i)
    