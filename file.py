#........................................file i/o..............................
#1.............................text files:.txt,.docx,.log etc....................
#2...........................binary files:.mp4,.mov,.png,.jpeg etc...............

#........................open, read & close file...............................
f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()

#.......................read......................
f=open("demo.txt","r")
data=f.read(5)
print(data)
f.close()

#.......................line......................
#data=f.read()
#print(data)
f=open("demo.txt","r")
line1=f.readline()
print(line1)
f.close()

#..................................writing..........................
f=open("demo.txt","w")
f.write("I want to learn javascrip tomorrow.123")
f.close()

f=open("demo.txt","a")
f.write("then I'll move to reactjs")#\n
f.close()


f=open("sample.txt","w")
f.close()


f=open("demo.txt","r+")
f.write("abc")
print(f.read())
f.close()


f=open("demo.txt","w+")
print(f.read())
f.write("abc")
f.close()
