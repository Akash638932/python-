'''
#q1 wap to ask the user to enter names of their 3 favorite movies & store them in a list.
movies=[]
list1=input("enter first favorite movies name:")
list2=input("enter second favorite movies name:")
list3=input("enter third favorite movies name:")
movies.append(list1)
movies.append(list2)
movies.append(list2)
print(movies)


#q2 wap to check if a list contains a palindrome of elements.(Hint:use copy()method)
list1=[1,2,1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("palindrame")
else:
    print(" not palindrame")
    
#q3 wap to count the number of students with the "A" grade in the following tuple.
#["c","d","a","a","b","b","a"]
tup=("c","d","a","a","b","b","a")
print(tup.count("a"))
'''
#q4 store the above values in a list & sort them from "A" to "D".
list=["c","d","a","a","b","b","a"]
list.sort()
print(list)