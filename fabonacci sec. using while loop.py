number=input("plz enter the no of in under u want:")
x=0
c=1  # 1,1,2,3,5,8,12
while x<=number:
    a=x
    x=x+c
    c=a
    if x<=number:     #we use if statement because an aditional tern was cooming which was more then number

        print x