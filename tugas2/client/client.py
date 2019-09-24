import Pyro4
import subprocess

def get_server():
    #ganti "localhost dengan ip yang akan anda gunakan sebagai server" 
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    return gserver

if __name__=='__main__':
    server = get_server()
    if server == None:
        exit()
    connected = True
    while connected:
        req = input ("> ").lower()
        req_split = req.split()
        if req_split[0] == 'ls':
            print(server.ls(req))
        elif req_split[0] == 'touch':
            print(server.touch(req))
        elif req_split[0] == 'rm':
            print(server.delete_handler(req))
        elif req_split[0] == 'rd':
            print(server.rd(req))
        elif req_split[0] == 'mv':
            print(server.mv(req))
        elif req_split[0] == 'exit':
            print(server.shutdown())
            connected = False
        else:
            print(server.command_not_found())
