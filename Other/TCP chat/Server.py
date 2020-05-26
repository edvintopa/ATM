import socket
import select
import sys
from thread import *

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(IP_address, Port)
