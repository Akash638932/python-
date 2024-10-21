#.................................................for loop..............................................
list=[1,2,3,4,5,6,7,8]
for i in list:
    print(i)
    
veggies=["potato","brijal","ladyfinger","cucumber"]
for i in veggies:
    print(i)
    
tup=(1,2,3,4,5)
for i in tup:
    print(i)



str="Akash"
for chr in str:
    if(chr =='s'):
        print("s found")
        break
    print(chr)
else:
    print("End")