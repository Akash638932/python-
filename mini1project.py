print("............................................random password Generator............................")
import random 
import string

pass_len = 8
charValues=string.ascii_letters + string.digits + string.punctuation
#list coprehension [function for i in range]
password="".join([random.choice(charValues) for i in range(pass_len)])





#password =""
#for i in range(pass_len):
#   password += random.choice(charValues)
print("your random password is:",password)