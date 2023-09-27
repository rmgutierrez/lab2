import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: www.google.com\n\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  #AF_INET => IPv4, SOCK_STREAM => TCP
        s.connect((host, port))
        s.send(request)
        s.shutdown(socket.SHUT_WR) # Socket can write #socket can read # So we shyt down the write side, and then get
        chunk = s.recv(BYTES_TO_READ)
        result = b'' + chunk

        while(len(chunk) > 0):
            chunk = s.recv(BYTES_TO_READ)
            result += chunk
        s.close() # The empty bytestring was sent
        return result

print(get("127.0.0.1", 8080))