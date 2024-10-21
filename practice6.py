'''
print("q1. print numbers from 1 to 100.")
i=1
while i <=100:
    print(i)
    i+=1
print("q2. print numbers from 100 to 1.")

i=100
while i >=1:
    print(i)
    i-=1


#q3 print the multiplication table of a number n.
n=int(input("enter number:"))
i=1
while i <=10:
    print(n*i)
    i+=1

#q4 print the elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]
num=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(num):
    print(num[idx])
    idx+=1
    
herose=["ironman","thor","superman","batman"]
i=0
while i<len(herose):
    print(herose[i])
    i+=1
'''
#q5 search for a number x in this tuple using loops:
#[1,4,9,16,25,36,49,64,81,100]

nums=(1,4,9,16,25,36,49,64,81,100)
x=36

i=0
while i < len(nums):
    if(nums[i] ==x):
        print("found at idx",i)
        break
    else:
        print("finding")
    i += 1