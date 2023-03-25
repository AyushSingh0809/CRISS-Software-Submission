import socket

serverIP="172.17.29.11"
serverPORT= 6000

serveraddress=(serverIP,serverPORT)
buffersize=1024

while True:
    UDPClientSocket= socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    message= "Ayush Singh_2022AAPS0222P"

    bytestosend=str.encode(message)
    UDPClientSocket.sendto(bytestosend,serveraddress)

