import re
import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org",80))
cmd="GET http://py4e-data.dr-chuck.net/comments_42.html HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)
l = list()
while True:
    data=mysock.recv(512)
    if (len(data)<1):
        break
    m=data.decode()
    q = m.rstrip()
    print(q)
    a = re.findall("[0-9]+", q)
    l.append(int(a))
    print(l)



mysock.close()