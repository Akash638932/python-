# waf to print the lenght of a list.(list is the parameter)
cities=["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes=["thor","ironman","captain","america","shaktiman"]

def print_len(list):
    print(len(list))
print_len(cities)
print_len(heroes)

#waf to print the elements of a list in a single line.(list is the parameter)
cities=["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes=["thor","ironman","captain","america","shaktiman"]

def print_len(list):
    print(len(list))
    
def print_list(list):
    for item in list:
        print(item,end=" ")
        
print_list(heroes)
print()

#waf to find the factorial of n.(n is the parameter)
def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
    
cal_fact(5)


#waf to convert USD to INR.

def converter(usd_val):
    inr_val=usd_val* 83
    print(usd_val,"USD=",inr_val,"INR")
    
converter(18)