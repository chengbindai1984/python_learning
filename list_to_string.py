

def list_to_string (mylist):
    mystring =''
    for i in range(len(mylist)):
       
       if i < len(mylist)-1:
           mystring+=mylist[i]
           mystring+=','
           print (mystring)
       elif i == len(mylist)-1:
           mystring+='and '+mylist[i]
           print (mystring)

    print (mystring)
        
    print (mylist)
    

spam = []

list_to_string (spam)