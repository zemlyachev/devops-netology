
# Домашнея работа к занятию 3. «Введение. Экосистема. Архитектура. Жизненный цикл Docker-контейнера»

## Задача 1

Сценарий выполнения задачи:

- создайте свой репозиторий на https://hub.docker.com;
- выберите любой образ, который содержит веб-сервер Nginx;
- создайте свой fork образа;
- реализуйте функциональность:
запуск веб-сервера в фоне с индекс-страницей, содержащей HTML-код ниже:
```
<html>
<head>
Hey, Netology
</head>
<body>
<h1>I’m DevOps Engineer!</h1>
</body>
</html>
```

Опубликуйте созданный fork в своём репозитории и предоставьте ответ в виде ссылки на https://hub.docker.com/username_repo.

> [https://hub.docker.com/r/kvintilian/ngnix-netology/tags](https://hub.docker.com/r/kvintilian/ngnix-netology/tags)
> 
> [Исходники](src_1)

## Задача 2

Посмотрите на сценарий ниже и ответьте на вопрос:
«Подходит ли в этом сценарии использование Docker-контейнеров или лучше подойдёт виртуальная машина, физическая машина? Может быть, возможны разные варианты?»

Детально опишите и обоснуйте свой выбор.

--

Сценарий:

- высоконагруженное монолитное Java веб-приложение;
> Виртуалка или физически сервер
- Nodejs веб-приложение;
> Контейнер
- мобильное приложение c версиями для Android и iOS;
> Что бы что: хранить артефакты, разрабатывать или крутить бекенд?
> Виртуалка, и можно контейнер для бека
- шина данных на базе Apache Kafka;
> Виртуалка
- Elasticsearch-кластер для реализации логирования продуктивного веб-приложения — три ноды elasticsearch, два logstash и две ноды kibana;
> Виртуалка
- мониторинг-стек на базе Prometheus и Grafana;
> Контейнер
- MongoDB как основное хранилище данных для Java-приложения;
> Виртуалка
- Gitlab-сервер для реализации CI/CD-процессов и приватный (закрытый) Docker Registry.
> Предоставляются в контейнерах, могут быть также установлены как и на виртуалку, так и на физический сервер

## Задача 3

- Запустите первый контейнер из образа ***centos*** c любым тегом в фоновом режиме, подключив папку ```/data``` из текущей рабочей директории на хостовой машине в ```/data``` контейнера.
- Запустите второй контейнер из образа ***debian*** в фоновом режиме, подключив папку ```/data``` из текущей рабочей директории на хостовой машине в ```/data``` контейнера.
- Подключитесь к первому контейнеру с помощью ```docker exec``` и создайте текстовый файл любого содержания в ```/data```.
- Добавьте ещё один файл в папку ```/data``` на хостовой машине.
- Подключитесь во второй контейнер и отобразите листинг и содержание файлов в ```/data``` контейнера.

> ```bash
> ➜  devops-netology git:(main) ✗ cd virtd/05-virt-03-docker
> ➜  05-virt-03-docker git:(main) ✗ cd src_3
> ➜  src_3 git:(main) ✗ mkdir data
> ➜  src_3 git:(main) ✗ ls
> data
> ➜  src_3 git:(main) ✗ docker pull centos
> Using default tag: latest
> latest: Pulling from library/centos
> a1d0c7532777: Pull complete
> Digest: sha256:a27fd8080b517143cbbbab9dfb7c8571c40d67d534bbdee55bd6c473f432b177
> Status: Downloaded newer image for centos:latest
> docker.io/library/centos:latest
> ➜  src_3 git:(main) ✗ docker pull debian
> Using default tag: latest
> latest: Pulling from library/debian
> 012c0b3e998c: Pull complete
> Digest: sha256:b4042f895d5d1f8df415caebe7c416f9dbcf0dc8867abb225955006de50b21f3
> Status: Downloaded newer image for debian:latest
> docker.io/library/debian:latest
> ➜  src_3 git:(main) ✗ docker run -v $PWD/data:/data --name centos-cont -d centos
> ec03751ed45b812bfb4df8dd5750210097aa27c20d49a8b6f1eec43b605e29bc
> ➜  src_3 git:(main) ✗ docker run -v $PWD/data:/data --name debian-cont -d debian
> 4c2fed2532a5d125e4d1b304206ff9eca0f19590ffbe6660706f020200428985
> ➜  src_3 git:(main) ✗ docker ps -a
> CONTAINER ID   IMAGE                          COMMAND                  CREATED              STATUS                      PORTS                           NAMES
> 4c2fed2532a5   debian                         "bash"                   27 seconds ago       Exited (0) 26 seconds ago                                   debian-cont
> ec03751ed45b   centos                         "/bin/bash"              46 seconds ago       Exited (0) 45 seconds ago                                   centos-cont
> ➜  src_3 git:(main) ✗ docker exec centos-cont /bin/bash -c "touch /data/somefile.txt"
> ➜  src_3 git:(main) ✗ touch /data/somefile2.txt
> ➜  src_3 git:(main) ✗ docker exec debian-cont ls -ll data/
> total 0
> -rw-r--r--. 1 root root 0 Sep 17 18:42 somefile.txt
> -rw-r--r--. 1 root root 0 Feb 13 18:43 somefile2.txt
> ➜  src_3 git:(main) ✗
> ```

