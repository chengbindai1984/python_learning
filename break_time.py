import webbrowser

import time 

total_breaks = 3 

break_count = 0

print (" This program started on " + time.ctime())
while True:
     if break_count < total_breaks:
        print ("Take a break")
        time.sleep(5) 
        webbrowser.open_new_tab("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
        break_count = break_count + 1
     else:
         break
   