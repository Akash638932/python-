#.................................................using for..............................................
#q1 print the elements the following list using a loop.
#[1,4,9,16,25,36,49,64,81,100]
elem=[1,4,9,16,25,36,49,64,81,100]
for i in elem:
    print(i)




#q2 search for a number x in this tuple using loops.
#[1,4,9,16,25,36,49,64,81,100]
elem=(1,4,9,16,25,36,49,64,81,100,49)
x=49
idx=0
for i in elem:
    if(i==x):
        print("number found at idx",idx)
        break
    idx+=1

