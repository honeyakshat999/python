database={'akshat':'admin','nimesh':'roomate'}
username = ['akshat','nimesh']
print database['akshat']
#pass=raw_input("passwd")

#value=raw_input("enter your login name:")
value = raw_input("enter yout username:")
value1 = raw_input("enter yout paasword:")



if value == username[0]:
    if value1 == database['akshat'] :
        print "you are loged in"
    else:
        print "incorrect password"
if value == username[1]:
    if value1 == database['nimesh']:
        print "you are akshat's roomate"
    else:
        print "wrong paasword"
