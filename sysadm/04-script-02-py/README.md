# Домашнее задание к занятию «Использование Python для решения типовых DevOps-задач»

### Инструкция к заданию

1. Установите Python 3 любой версии.
2. Скопируйте в свой .md-файл содержимое этого файла, исходники можно посмотреть [здесь](https://raw.githubusercontent.com/netology-code/sysadm-homeworks/devsys10/04-script-02-py/README.md).
3. Заполните недостающие части документа решением задач — заменяйте `???`, остальное в шаблоне не меняйте, чтобы не сломать форматирование текста, подсветку синтаксиса. Вместо логов можно вставить скриншоты по желанию.
4. Для проверки домашнего задания в личном кабинете прикрепите и отправьте ссылку на решение в виде md-файла в вашем репозитории.
5. Любые вопросы по выполнению заданий задавайте в чате учебной группы или в разделе «Вопросы по заданию» в личном кабинете.

## Задание 1

Есть скрипт:

```python
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
```

### Вопросы:

| Вопрос                                         | Ответ                                |
|------------------------------------------------|--------------------------------------|
| Какое значение будет присвоено переменной `c`? | никакое, ошибка из-за различия типов |
| Как получить для переменной `c` значение 12?   | `str(a) + b`                         |
| Как получить для переменной `c` значение 3?    | `a + int(b)`                         |

---

## Задание 2

Мы устроились на работу в компанию, где раньше уже был DevOps-инженер. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся.

Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?

```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
```

### Ваш скрипт:

```python
#!/usr/bin/env python3

import os
import re

path = os.path.join('~/netology/sysadm-homeworks')
bash_command = [f"cd {path}", "git status"]
modify_pat_list = ["modified:", "изменено:"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if any(substring in result for substring in modify_pat_list):
        prepare_result = re.sub('|'.join(modify_pat_list), "", result).strip()
        print(os.path.join(path, prepare_result))


```

### Вывод скрипта при запуске во время тестирования:

```
/usr/local/bin/python3.9 /Users/andrej/netology/sysadm-homeworks/sysadm/04-script-02-py/test.py 
~/netology/sysadm-homeworks/sysadm/03-sysadmin-07-net/README.md

Process finished with exit code 0
```

---

## Задание 3

Доработать скрипт выше так, чтобы он не только мог проверять локальный репозиторий в текущей директории, но и умел воспринимать путь к репозиторию, который мы передаём, как входной параметр. Мы точно знаем, что начальство будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

### Ваш скрипт:

```python
#!/usr/bin/env python3

import os
import re
import sys

try:
    path = os.path.join(sys.argv[1])
except IndexError:
    print('Illegal arguments')
    sys.exit()
bash_command = [f"cd {path}", "git status"]
modify_pat_list = ["modified:", "изменено:"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
try:
    if ".git" not in os.listdir(path):
        print(f'Directory "{path}" is not a git repository')
        sys.exit()
    for result in result_os.split('\n'):
        if any(substring in result for substring in modify_pat_list):
            prepare_result = re.sub('|'.join(modify_pat_list), "", result).strip()
            print(os.path.join(path, prepare_result))
except FileNotFoundError:
    print(f'Directory "{path}" not found')
except NotADirectoryError:
    print('The passed value is not a directory')

```

### Вывод скрипта при запуске во время тестирования:

```
/usr/local/bin/python3.9 /Users/andrej/Documents/GitHub/devops-netology/sysadm/04-script-02-py/test.py /Users/andrej/Documents/GitHub/devops-netology/ 
/Users/andrej/Documents/GitHub/devops-netology/sysadm/03-sysadmin-07-net/README.md

Process finished with exit code 0
```

---

## Задание 4

Наша команда разрабатывает несколько веб-сервисов, доступных по HTTPS. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис.

Проблема в том, что отдел, занимающийся нашей инфраструктурой, очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS-имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков.

Мы хотим написать скрипт, который:

- опрашивает веб-сервисы;
- получает их IP;
- выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>.

Также должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена — оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: `drive.google.com`, `mail.google.com`, `google.com`.

### Ваш скрипт:

```python
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

```

### Вывод скрипта при запуске во время тестирования:

```
/usr/local/bin/python3.9 /Users/andrej/Documents/GitHub/devops-netology/sysadm/04-script-02-py/test.py
drive.google.com     - 142.250.150.194
mail.google.com      - 216.58.210.133
google.com           - 74.125.205.113
drive.google.com     - 142.250.150.194
mail.google.com      - 216.58.210.133
google.com           - 74.125.205.113
[ERROR] drive.google.com IP mismatch: 142.250.150.194 -> 64.233.164.194
drive.google.com     - 64.233.164.194
mail.google.com      - 216.58.210.133
google.com           - 74.125.205.113
drive.google.com     - 64.233.164.194
mail.google.com      - 216.58.210.133
google.com           - 74.125.205.113

```

