# Домашнее задание к занятию «Элементы безопасности информационных систем»


### Цель задания

В результате выполнения задания вы: 

* настроите парольный менеджер, что позволит не использовать один и тот же пароль на все ресурсы и удобно работать со множеством паролей;
* настроите веб-сервер на работу с HTTPS. Сегодня HTTPS является стандартом в интернете. Понимание сути работы центра сертификации, цепочки сертификатов позволит сконфигурировать SSH-клиент на работу с разными серверами по-разному, что даёт большую гибкость SSH-соединений. Например, к некоторым серверам мы можем обращаться по SSH через приложения, где недоступен ввод пароля;
* поработаете со сбором и анализом трафика, которые необходимы для отладки сетевых проблем.


### Инструкция к заданию

1. Создайте .md-файл для ответов на задания в своём репозитории, после выполнения прикрепите ссылку на него в личном кабинете.
2. Любые вопросы по выполнению заданий задавайте в чате учебной группы или в разделе «Вопросы по заданию» в личном кабинете.

### Дополнительные материалы для выполнения задания

1. [SSL + Apache2](https://digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-20-04).

------

## Задание

1. Установите плагин Bitwarden для браузера. Зарегестрируйтесь и сохраните несколько паролей.
![img.png](img.png)
![img_1.png](img_1.png)
2. Установите Google Authenticator на мобильный телефон. Настройте вход в Bitwarden-акаунт через Google Authenticator OTP.
![img_2.png](img_2.png)
![img_3.png](img_3.png)
3. Установите apache2, сгенерируйте самоподписанный сертификат, настройте тестовый сайт для работы по HTTPS.

4. Проверьте на TLS-уязвимости произвольный сайт в интернете (кроме сайтов МВД, ФСБ, МинОбр, НацБанк, РосКосмос, РосАтом, РосНАНО и любых госкомпаний, объектов КИИ, ВПК и т. п.).

5. Установите на Ubuntu SSH-сервер, сгенерируйте новый приватный ключ. Скопируйте свой публичный ключ на другой сервер. Подключитесь к серверу по SSH-ключу.
 
6. Переименуйте файлы ключей из задания 5. Настройте файл конфигурации SSH-клиента так, чтобы вход на удалённый сервер осуществлялся по имени сервера.

7. Соберите дамп трафика утилитой tcpdump в формате pcap, 100 пакетов. Откройте файл pcap в Wireshark.

```bash
sudo tcpdump -c 100 -w dump.pcap
Password:
tcpdump: data link type PKTAP
tcpdump: listening on pktap, link-type PKTAP (Apple DLT_PKTAP), snapshot length 524288 bytes
100 packets captured
451 packets received by filter
0 packets dropped by kernel
```

![img.png](wireshark.png)

*В качестве решения приложите: скриншоты, выполняемые команды, комментарии (при необходимости).*

 ---
 
## Задание со звёздочкой* 

Это самостоятельное задание, его выполнение необязательно.

8. Просканируйте хост scanme.nmap.org. Какие сервисы запущены?

9. Установите и настройте фаервол UFW на веб-сервер из задания 3. Откройте доступ снаружи только к портам 22, 80, 443.

----

### Правила приёма домашнего задания

В личном кабинете отправлена ссылка на .md-файл в вашем репозитории.

-----

### Критерии оценки

Зачёт:

* выполнены все задания;
* ответы даны в развёрнутой форме;
* приложены соответствующие скриншоты и файлы проекта;
* в выполненных заданиях нет противоречий и нарушения логики.

На доработку:

* задание выполнено частично или не выполнено вообще;
* в логике выполнения заданий есть противоречия и существенные недостатки.  
 
Обязательными являются задачи без звёздочки. Их выполнение необходимо для получения зачёта и диплома о профессиональной переподготовке.

Задачи со звёздочкой (*) являются дополнительными или задачами повышенной сложности. Они необязательные, но их выполнение поможет лучше разобраться в теме.