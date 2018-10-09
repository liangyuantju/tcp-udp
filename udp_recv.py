from socket import *
import base64

host = ''  # 监听所有的ip
port = 54321
bufsize = 1024
addr = (host, port)

udpServer = socket(AF_INET, SOCK_DGRAM)
udpServer.bind(addr)

while True:
    print('Waiting for connection....')
    data_origin, addr = udpServer.recvfrom(bufsize)
    # 处理数据
    data = base64.b64decode(data_origin)
    print('recv ---- \n', data)



