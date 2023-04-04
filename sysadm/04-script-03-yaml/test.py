#!/usr/bin/env python3

import time
import socket
import json
import yaml
import os

services = ['drive.google.com', 'mail.google.com', 'google.com']
ip_hosts = {}
out_dir = 'out/'


def save_to_file(_service, _ip):
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    with open(out_dir + _service + '.yml', 'w') as yml:
        yaml.safe_dump([{_service: _ip}], yml)
    with open(out_dir + _service + '.json', 'w') as js:
        json.dump({_service: _ip}, js)


while True:
    for service in services:
        ip = socket.gethostbyname(service)
        if service not in ip_hosts.keys():
            ip_hosts[service] = ip
            save_to_file(service, ip)
        else:
            if ip != ip_hosts[service]:
                print(f'[ERROR] {service} IP mismatch: {ip_hosts[service]} -> {ip}')
                ip_hosts[service] = ip
                save_to_file(service, ip)
        print(f'{service:20} - {ip}')
    time.sleep(10)
