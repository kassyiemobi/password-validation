#building a password that is at least 8 characters long.
#it should end with a number

import re
print('enter a strong password')

password= input()
if  re.match(r"[A-Za-z0-9@#$%^&+=]{8,}\d",password):
    print('password accepted')

else:
    print("enter a better password")



