
def alphabet_position(text):

    import re
    textList=re.findall(r"[a-z]",text.lower())
    textNumber=[]
    for i in textList:
        textNumber.append(ord(i)-96)
    return " ".join(str(e) for e in textNumber) 

alphabet_position("The sunset sets at twelve o' clock.")

# textNumber = map(lambda x: ord(x), textList)

def alphabet_position(text):
    
    import re
    textNumber = map(lambda x: ord(x)-96, re.findall(r"[a-z]",text.lower())
    return " ".join(str(e) for e in textNumber) 

alphabet_position("The sunset sets at twelve o' clock.")
# textList = (lambda x: ord(x), list(re.findall(r"[a-zA-Z]",text)))


