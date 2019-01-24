#!/usr/bin/python2.7
import socket


class connection:
    def connection(ip, port, user, cha):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(9)
        sock.connect((ip, int(port)))
        sock.sendto(cha.encode('utf-8'), ip, port)

        cdata = sock.recv(1024)

        sock.connect((ip, int(port)))
        sock.sendto(passw.encode('utf-8'), (user, cha))

        pdata = sock.recv(1024)
        socket.timeout(9)


class Brute_force:
    def iter_all_string():
        length(1)
        while True:
            for s in iter_all_string(cha, repeat=length):
                yield "".join(s)
            length += 1

    for s in iter_all_string():
        print(s)
        if s == passw:
            print('Password is {}'.format(s))
            break
    print cdata, pdata

    def target():
        ip = raw_input("Enter the IP : ")
        port = raw_input("Enter the Port : ")
        user = raw_input("Enter user : ")
        passw = list(map(str, "A-Za-z0-9\./[]!@#$%"))
        characters = passw
        datalogin = (ip, port, user)
        s = socket
        print (" [*] IP selected: "), ip
        print (" [*] PORT selected (Default 21): "), port
        print (" [*] User selected: "), user
        print (" [*] Information selected: ")
        print raw_input("Press any key to start... ")