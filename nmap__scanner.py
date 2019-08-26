import nmap
#creating an object
ob=nmap.PortScanner()
print (ob.nmap_version())
#h1=input("enter the hostip")

ob.scan('10.2.65.2','22-443','-v --version-all')  #scan(host,port,method)
print ob.scaninfo()
print ob.csv() # this is main it holds all details of scan




#nmap -oX - -p 22-443 127.0.0.1

print "-----------------------------------------------------------------------------"
print ob.scanstats() #this tells about scan statics
print ob.all_hosts() #this will display all the hosts
print ob['10.2.65.2'].state() #this tells is system is up or not
print ob['10.2.65.2'].all_protocols() #this tell which protocol

print ob['10.2.65.2']['tcp'].keys() # this tells us which ports are open

ak =ob['10.2.65.2'].has_tcp(139)  # this tells about is a specific port is open or not
print ak