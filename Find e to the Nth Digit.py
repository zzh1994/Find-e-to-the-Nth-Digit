
# coding: utf-8

# In[ ]:


import math

while True:
    try:
        q = int(input("No. of decimal points for e: "))
    except:
        print ("Please input an integer")
    else:
        print (f"{math.e:1.{q}f}")
        
        r = ""
        while not (r == 'y' or r == 'n'):
            r = input("Calculate again? Y or N: ").lower()
        
        if r == 'y':
            continue
        else:
            print ("Thanks for using!")
            break

