
    
 myRcv70=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 myRcv70.bind(('128.123.131.66', 25001))
 
 myRcv211=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 myRcv211.bind(('128.123.131.66', 25002))
 
 myRcv199=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 myRcv211.bind(('128.123.131.66', 25003))
 
 data = myRcv70.recvfrom(1024)
 values70 = array.array('d', data[0])
 print(values70)
    
 data = myRcv211.recvfrom(1024)
 values211 = array.array('d', data[0])
 print(values211)
 
 data = myRcv199.recvfrom(1024)
 values199 = array.array('d', data[0])
 print(values199)
 
