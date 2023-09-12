# Домашнее задание к занятию "Компьютерные сети, лекция 3"

## Задание

https://github.com/netology-code/sysadm-homeworks/blob/devsys10/03-sysadmin-08-net/README.md

## Решение

### 1. Подключитесь к публичному маршрутизатору в интернет. Найдите маршрут к вашему публичному IP

```bash
telnet route-views.routeviews.org
Username: rviews
show ip route x.x.x.x/32
show bgp x.x.x.x/32
```

> ```bash
> vagrant@vagrant:~$ telnet route-views.routeviews.org
> Trying 128.223.51.103...
> Connected to route-views.routeviews.org.
> Escape character is '^]'.
> C
> **********************************************************************
>
>                    RouteViews BGP Route Viewer
>                    route-views.routeviews.org
>
> route views data is archived on http://archive.routeviews.org
>
> This hardware is part of a grant by the NSF.
> Please contact help@routeviews.org if you have questions, or
> if you wish to contribute your view.
>
> This router has views of full routing tables from several ASes.
> The list of peers is located at http://www.routeviews.org/peers
> in route-views.oregon-ix.net.txt
>
> NOTE: The hardware was upgraded in August 2014.  If you are seeing
> the error message, "no default Kerberos realm", you may want to
> in Mac OS X add "default unset autologin" to your ~/.telnetrc
>
> To login, use the username "rviews".
>
> **********************************************************************
>
> User Access Verification
>
> Username: rviews
>
> route-views>show ip route 46.160.224.196
> Routing entry for 46.160.224.0/21
>  Known via "bgp 6447", distance 20, metric 0
>  Tag 3303, type external
>  Last update from 217.192.89.50 1w0d ago
>  Routing Descriptor Blocks:
>  * 217.192.89.50, from 217.192.89.50, 1w0d ago
>      Route metric is 0, traffic share count is 1
>      AS Hops 4
>      Route tag 3303
>      MPLS label: none
>
> route-views>show bgp 46.160.224.196
> BGP routing table entry for 46.160.224.0/21, version 2667864299
> Paths: (21 available, best #19, table default)
>  Not advertised to any peer
>  Refresh Epoch 1
>  20912 6939 35598 35539 35539 35539 35539 35539
>    212.66.96.126 from 212.66.96.126 (212.66.96.126)
>      Origin IGP, localpref 100, valid, external
>      Community: 20912:65016
>      path 7FE14CDD6150 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  6939 35598 35539 35539 35539 35539 35539
>    64.71.137.241 from 64.71.137.241 (216.218.253.53)
>      Origin IGP, localpref 100, valid, external
>      path 7FE164B9C1C8 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  8283 28917 35539 35539
>    94.142.247.3 from 94.142.247.3 (94.142.247.3)
>      Origin IGP, metric 0, localpref 100, valid, external
>      Community: 0:6939 0:16276 0:31500 0:49981 8283:1 8283:101 8283:102 28917:2000 28917:2299 28917:5110
>      unknown transitive attribute: flag 0xE0 type 0x20 length 0x30
>        value 0000 205B 0000 0000 0000 0001 0000 205B
>              0000 0005 0000 0001 0000 205B 0000 0005
>              0000 0002 0000 205B 0000 0008 0000 0732
>
>      path 7FE0DBECB348 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  53767 6939 35598 35539 35539 35539 35539 35539
>    162.251.163.2 from 162.251.163.2 (162.251.162.3)
>      Origin IGP, localpref 100, valid, external
>      Community: 53767:2000
>      path 7FE0F8416F28 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  3549 3356 12389 35598 35539 35539 35539 35539 35539
>    208.51.134.254 from 208.51.134.254 (67.16.168.191)
>      Origin IGP, metric 0, localpref 100, valid, external
>      Community: 3356:2 3356:22 3356:100 3356:123 3356:501 3356:901 3356:2065 3549:2581 3549:30840 35598:100
>      path 7FE02768C5F8 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  19214 3257 28917 35539 35539
>    208.74.64.40 from 208.74.64.40 (208.74.64.40)
>      Origin IGP, localpref 100, valid, external
>      Community: 3257:4000 3257:8092 3257:50001 3257:50111 3257:54800 3257:54801
>      path 7FE0A8914188 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 2
>  2497 3257 28917 35539 35539
>    202.232.0.2 from 202.232.0.2 (58.138.96.254)
>      Origin IGP, localpref 100, valid, external
>      path 7FE1333EEAE8 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  4901 6079 6939 35598 35539 35539 35539 35539 35539
>    162.250.137.254 from 162.250.137.254 (162.250.137.254)
>      Origin IGP, localpref 100, valid, external
>      Community: 65000:10100 65000:10300 65000:10400
>      path 7FE128446EF8 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  3356 12389 35598 35539 35539 35539 35539 35539
>    4.68.4.46 from 4.68.4.46 (4.69.184.201)
>      Origin IGP, metric 0, localpref 100, valid, external
>      Community: 3356:2 3356:22 3356:100 3356:123 3356:501 3356:901 3356:2065 35598:100
>      path 7FE0A27CE8A8 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  3561 3910 3356 12389 35598 35539 35539 35539 35539 35539
>    206.24.210.80 from 206.24.210.80 (206.24.210.80)
>      Origin IGP, localpref 100, valid, external
>      path 7FE0EE2CF290 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  101 6939 35598 35539 35539 35539 35539 35539
>    209.124.176.223 from 209.124.176.223 (209.124.176.223)
>      Origin IGP, localpref 100, valid, external
>      Community: 101:20300 101:22100
>      path 7FE02F39D5D0 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  7018 3257 28917 35539 35539
>    12.0.1.63 from 12.0.1.63 (12.0.1.63)
>      Origin IGP, localpref 100, valid, external
>      Community: 7018:5000 7018:37232
>      path 7FE120C43B88 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  852 6939 35598 35539 35539 35539 35539 35539
>    154.11.12.212 from 154.11.12.212 (96.1.209.43)
>      Origin IGP, metric 0, localpref 100, valid, external
>      path 7FE184473778 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  57866 28917 35539 35539
>    37.139.139.17 from 37.139.139.17 (37.139.139.17)
>      Origin IGP, metric 0, localpref 100, valid, external
>      Community: 0:6939 0:16276 0:31500 0:49981 28917:2000 28917:2299 28917:5110 57866:200 65102:41441 65103:1 65104:31
>      unknown transitive attribute: flag 0xE0 type 0x20 length 0x30
>        value 0000 E20A 0000 0065 0000 00C8 0000 E20A
>              0000 0066 0000 A1E1 0000 E20A 0000 0067
>              0000 0001 0000 E20A 0000 0068 0000 001F
>
>      path 7FE11E0C5AF0 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  49788 6939 35598 35539 35539 35539 35539 35539
>    91.218.184.60 from 91.218.184.60 (91.218.184.60)
>      Origin IGP, metric 0, localpref 100, valid, external
>      Community: 49788:1000
>      path 7FE04238B320 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  3257 28917 35539 35539
>    89.149.178.10 from 89.149.178.10 (213.200.83.26)
>      Origin IGP, metric 10, localpref 100, valid, external
>      Community: 3257:4000 3257:8092 3257:50001 3257:50111 3257:54800 3257:54801
>      path 7FE000F7A618 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  3333 1257 28917 35539 35539
>    193.0.0.56 from 193.0.0.56 (193.0.0.56)
>      Origin IGP, localpref 100, valid, external
>      Community: 1257:50 1257:51 1257:2000 1257:3428 1257:4103 28917:2000 28917:2299 28917:5110
>      path 7FE169E3E028 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  1351 6939 35598 35539 35539 35539 35539 35539
>    132.198.255.253 from 132.198.255.253 (132.198.255.253)
>      Origin IGP, localpref 100, valid, external
>      path 7FE123996FC8 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  3303 28917 35539 35539
>    217.192.89.50 from 217.192.89.50 (138.187.128.158)
>      Origin IGP, localpref 100, valid, external, best
>      Community: 3303:1004 3303:1006 3303:1030 3303:3056 28917:2000 28917:2299 28917:5110
>      path 7FE11968A208 RPKI State valid
>      rx pathid: 0, tx pathid: 0x0
>  Refresh Epoch 1
>  20130 23352 3257 28917 35539 35539
>    140.192.8.16 from 140.192.8.16 (140.192.8.16)
>      Origin IGP, localpref 100, valid, external
>      path 7FE0FBD19EF0 RPKI State valid
>      rx pathid: 0, tx pathid: 0
>  Refresh Epoch 1
>  3267 35598 35539 35539 35539 35539 35539
>    194.85.40.15 from 194.85.40.15 (185.141.126.1)
>      Origin IGP, metric 0, localpref 100, valid, external
>      path 7FE17845E968 RPKI State valid
>      rx pathid: 0, tx pathid: 0
> ```

### 2. Создайте dummy0 интерфейс в Ubuntu. Добавьте несколько статических маршрутов. Проверьте таблицу маршрутизации.

### 3. Проверьте открытые TCP порты в Ubuntu, какие протоколы и приложения используют эти порты? Приведите несколько примеров.

> ```bash
> vagrant@vagrant:~$ ss -ltpn
> State      Recv-Q     Send-Q         Local Address:Port           Peer Address:Port     Process
> LISTEN     0          4096           127.0.0.53%lo:53                  0.0.0.0:*
> LISTEN     0          128                  0.0.0.0:22                  0.0.0.0:*
> LISTEN     0          128                     [::]:22                     [::]:*
> ```

### 4. Проверьте используемые UDP сокеты в Ubuntu, какие протоколы и приложения используют эти порты?

> ```bash
> vagrant@vagrant:~$ ss -lupn
> State      Recv-Q     Send-Q          Local Address:Port          Peer Address:Port     Process
> UNCONN     0          0               127.0.0.53%lo:53                 0.0.0.0:*
> UNCONN     0          0              10.0.2.15%eth0:68                 0.0.0.0:*
> ```

### 5. Используя diagrams.net, создайте L3 диаграмму вашей домашней сети или любой другой сети, с которой вы работали.
