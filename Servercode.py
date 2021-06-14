import socket
import cv2
import pickle
import struct

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('Server ip :',host_ip)
port = 9999
socket_address = ('192.168.99.1',port)
server_socket.bind(socket_address)
server_socket.listen(5)
while True:
    client_socket,addr = server_socket.accept()
    print('GOT CONNECTION FROM:',addr)
    if client_socket:
        cap = cv2.VideoCapture(0)
        
        while(cap.isOpened()):
            img,frame = cap.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            cv2.COLOR_BGR2GRAY
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow('Sending Video',frame)
            key = cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                client_socket.close()
