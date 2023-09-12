#!/usr/bin/env python3

import time
import socket

services = ('drive.google.com', 'mail.google.com', 'google.com')
ip_hosts = {}

while True:
    for service in services:
        ip = socket.gethostbyname(service)

        if service not in ip_hosts.keys():
            ip_hosts[service] = ip

        else:
            if ip != ip_hosts[service]:
                print(f'[ERROR] {service} IP mismatch: {ip_hosts[service]} -> {ip}')
                ip_hosts[service] = ip
        print(f'{service:20} - {ip}')
    time.sleep(10)
