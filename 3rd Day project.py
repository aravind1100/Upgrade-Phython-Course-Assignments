#6 Digit random OTP

import random as r
import string as s

my_list =list(s.ascii_letters + s.digits)
for i in range(6) :
      print( r.choice(my_list), end = '')
       
       
    
