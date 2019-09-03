class pink: # basic class declarationssss
    a=20
    def akshat(self):
        print "akshat"
        print self.a  #to use variale from above in function you have to use self keyword
    #akshat()

ob=pink()
op=pink() #here we define object of class pink
print ob.akshat()
print ob.a #here u can access functions and variable using object.
op.a=10
print op.a
