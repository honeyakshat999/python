import nmap
#creating an object
ob=nmap.PortScanner()
print (ob.nmap_version())
#h1=input("enter the hostip")

ob.scan('52.66.187.102','1-1024','-v')  #scan(host,port,method)
print ob.scaninfo()
print ob.csv() # this is main it holds all details of scan


