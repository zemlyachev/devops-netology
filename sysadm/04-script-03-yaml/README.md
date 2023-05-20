# Домашнее задание к занятию «Языки разметки JSON и YAML»

## Задание 1

Мы выгрузили JSON, который получили через API-запрос к нашему сервису:

```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```

Нужно найти и исправить все ошибки, которые допускает наш сервис.

### Ваш скрипт

```json
{
    "info": "Sample JSON output from our service\\t",
    "elements": [
        {
            "name": "first",
            "type": "server",
            "ip": 7175
        },
        {
            "name": "second",
            "type": "proxy",
            "ip": "71.78.22.43"
        }
    ]
} 
```

---

## Задание 2

В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML-файлов, описывающих наши сервисы.

Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`.

Формат записи YAML по одному сервису: `- имя сервиса: его IP`.

Если в момент исполнения скрипта меняется IP у сервиса — он должен так же поменяться в YAML и JSON-файле.

### Ваш скрипт

[Скрипт](test.py)

```python
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

```

### Вывод скрипта при запуске во время тестирования

```shell
/usr/local/bin/python3.9 /Users/andrej/Documents/GitHub/devops-netology/sysadm/04-script-03-yaml/test.py 
drive.google.com     - 173.194.73.194
mail.google.com      - 216.58.209.197
google.com           - 216.58.210.142
drive.google.com     - 173.194.73.194
mail.google.com      - 216.58.209.197
google.com           - 216.58.210.142
drive.google.com     - 173.194.73.194
mail.google.com      - 216.58.209.197
google.com           - 216.58.210.142
drive.google.com     - 173.194.73.194
mail.google.com      - 216.58.209.197
google.com           - 216.58.210.142
drive.google.com     - 173.194.73.194
mail.google.com      - 216.58.209.197
google.com           - 216.58.210.142
drive.google.com     - 173.194.73.194
mail.google.com      - 216.58.209.197
google.com           - 216.58.210.142
drive.google.com     - 173.194.73.194
mail.google.com      - 216.58.209.197
google.com           - 216.58.210.142
drive.google.com     - 173.194.73.194
mail.google.com      - 216.58.209.197
google.com           - 216.58.210.142
drive.google.com     - 173.194.73.194
mail.google.com      - 216.58.209.197
google.com           - 216.58.210.142
```

### JSON-файл(ы), который(е) записал ваш скрипт

#### drive.google.com.json
```json
{"drive.google.com": "173.194.73.194"}
```
#### google.com.json
```json
{"google.com": "216.58.210.142"}
```
#### mail.google.com.json
```json
{"mail.google.com": "216.58.209.197"}
```

### YAML-файл(ы), который(е) записал ваш скрипт

#### drive.google.com.yml
```yaml
- drive.google.com: 173.194.73.194
```
#### google.com.yml
```yaml
- google.com: 216.58.210.142
```
#### mail.google.com.yml
```yaml
- mail.google.com: 216.58.209.197
```

[Все файлы](out/)

---

