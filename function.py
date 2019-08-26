def func():           #defining a function
    print "i am using a function"

func() #calling a function

#passing vales in function
def calc(a,b):
    print "choose from the following:\n""1.addition\n""2.substraction""\n3.multiplication""\n4.division"
    choice=input()
    if choice<0:
        print "wrong choice"
    if choice==1:
        print "result is ",a+b
    if choice==2:
        print "result is ",a-b
    if choice==3:
        print "result is ",a*b
    if choice==4:
        print "result is ",a/b
        print "remaineder is ",a%b
    if choice<4:
        print "wrong choice"
a=input("enter first value:")
b=input("enter second value:")

calc(a,b)
#print d


print "tnx for using us"

print "function using return "

def addition():
    b = input("input a first value:")
    a=input("input the second value:")

    print "result is ",a+b

addition()