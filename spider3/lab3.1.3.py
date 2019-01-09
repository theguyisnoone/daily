import socket
import urllib.request
import urllib.error

try:
    response =urllib.request.urlopen('http://httpbin.org/get',timeout=0.01)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TimeOut')
