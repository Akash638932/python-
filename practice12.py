#q1.create a new file "practice.txt" using python .add the following data in it .
'''
hi everyone
we are learning file i/o
using java.
i like programming in java.
'''
with open ("practice.txt","w") as f:
    f.write("hi everyone \n we are learnning file I/o \n")
    f.write("using java.\n i like programming in java.")
    

#q2 waf that replace all occurrences of "java"with "python" in above file.
with open ("practice.txt","w") as f:
    data=f.read()
    
new_data=data.replace("java","python")
print(new_data)

'''
with open("practice.txt","w")as f:
f.write(new_data)
'''


#q3 search if the word "learning" exists in the file or not.
#def check_for_word():
word="learning"
with open("practice.txt","r") as f:
        data=f.read()
        if(data.find(word)!=-1):
            print("found")
        else:
            print("not found")
            
#check_for_word()


#q4 waf to find in which line of the file does the word "learning" occur first.
#print -1 if word not found.
def check_for_word():
    word="learning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(word in data):
            print("found")
        else:
            print("not found")
            
            
def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open ("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1
    return -1
check_for_line()
    
#q5 from a file containing numbers seprated by comma ,print  the count of even numbers.
with open("practice1.txt","r") as f:
    data=f.read()
print(data)

num=""
for i in range(len(data)):
    if(data[i]==","):
        print(int(num))
        num=" "
    else:
        num += data[i]
print("..................................................")
count=0
with open("practice1.txt","r") as f:
    data=f.read()
    
    nums=data.splist(",")
    for val in nums:
        if(int(val) % 2==0):
            count +=1
print(count)
