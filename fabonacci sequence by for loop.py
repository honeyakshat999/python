# 1 1 2 3 5 8 13
n=input("plz enter the no of rows u time u want:")
p=0
a=1
c=0
for w in range(0,n+1):
    c=p      #c=1
    p=p+a  #p= 1,2,3,5
             #a= 1,1,2
    a=c
    print p





