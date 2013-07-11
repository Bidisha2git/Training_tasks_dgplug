Solution

-------------

The code is all about printing the contents of the mount command.

At 1st we open the file /proc/mounts and then make changes so that the output comes out to be the contents of the mount command.
Then we read the file line by line by the function readline().
then looping through each line we insert and delete certain elements as is given in the code below.


Code

----------

#!/usr/bin/env python

f = open("/proc/mounts")#opens the file /proc/mounts

l = f.readlines()# reads the file line by line

for i in l[1:]:# for loop which ignores the first line of the file 
    
    a = i.split(" ")#splits the file line by line according to spaces
    
    del a[-2]#deletes the  second last zero from the file
    
    del a[-1]#deletes the last zero from the file
    
    a.insert(2,"type ")# the string "type" is inserted in index 2
    
    a.insert(1,"on")# the string "on" is inserted in index 1
    
    a.insert(5,"(")# the opening bracket "(" is inserted in the 5th index
    
    a.insert(7,")")# the closing bracket ")" is inserted in the 7th index
    
    str = " ".join(a)# the splitted string is joined using the join() functi        on
    
    print str #the required output is printed; for loop ends
    
    f.close()# file is closed


Link

------------

The link to the code is:

https://github.com/Bidisha2git/Training_tasks_dgplug/blob/master/mount.py
