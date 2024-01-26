# logging level 1


# Basic as it is, I started logging my programs with a simple print()

y = 1
if y < 100:
    y +=1
    print(y)

# For small tests... perfect! 

# But it also lacks flexibility, you need to implement everything on your 
# once and once again, and no mention if you happen to change your logging format
    
# let's say you have 100 log comments along your code, if you want to change
# the log format, you will have to check 100 lines of code that are spread
# in many files...so lets keep findinf better ways..