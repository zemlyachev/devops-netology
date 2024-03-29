
# Домашняя работа к занятию 1.  «Введение в виртуализацию. Типы и функции гипервизоров. Обзор рынка вендоров и областей применения»


## Задача 1

Опишите кратко, в чём основное отличие полной (аппаратной) виртуализации, паравиртуализации и виртуализации на основе ОС.

> - Аппаратная виртуализация - гипервизор устанавливается непосредственно на железо 
> - Паравиртуализация - гипервизор устанавливается на хостовую ОС и работает как системная служба 
> - Виртуализация уровня ОС - использование контейнерами реального железа без гипервизора, единая ОС

## Задача 2

Выберите один из вариантов использования организации физических серверов в зависимости от условий использования.

Организация серверов:

- физические сервера,
- паравиртуализация,
- виртуализация уровня ОС.

Условия использования:

- высоконагруженная база данных, чувствительная к отказу;
- различные web-приложения;
- Windows-системы для использования бухгалтерским отделом;
- системы, выполняющие высокопроизводительные расчёты на GPU.

Опишите, почему вы выбрали к каждому целевому использованию такую организацию.

>- высоконагруженная база данных, чувствительная к отказу:
>  - физические сервера, производительность и отказоустойчивость
>- различные web-приложения:
>  - виртуализация уровня ОС, быстрое разворачивание и изолирование приложений
>- Windows-системы для использования бухгалтерским отделом:
>  - паравиртуализация, либо физические, в зависимости от требований конкретного ПО
>- системы, выполняющие высокопроизводительные расчёты на GPU: 
>  - физические сервера, прямой доступ к железу

## Задача 3

Выберите подходящую систему управления виртуализацией для предложенного сценария. Детально опишите ваш выбор.

Сценарии:

1. 100 виртуальных машин на базе Linux и Windows, общие задачи, нет особых требований. Преимущественно Windows based-инфраструктура, требуется реализация программных балансировщиков нагрузки, репликации данных и автоматизированного механизма создания резервных копий.
> Hyper-V и vSphere подходят для Windows и Linux. Есть программные балансировщики нагрузки, репликации данных и автоматизированный механизм создания резервных копий.

2. Требуется наиболее производительное бесплатное open source-решение для виртуализации небольшой (20-30 серверов) инфраструктуры на базе Linux и Windows виртуальных машин.
> Подойдет Proxmox или KVM, можно запускать Windows и Linux.

3. Необходимо бесплатное, максимально совместимое и производительное решение для виртуализации Windows-инфраструктуры.
> Hyper-V Server, бесплатное решение от MicroSoft

4. Необходимо рабочее окружение для тестирования программного продукта на нескольких дистрибутивах Linux.
> Docker для автоматического, VirtualBox

## Задача 4

Опишите возможные проблемы и недостатки гетерогенной среды виртуализации (использования нескольких систем управления виртуализацией одновременно) и что необходимо сделать для минимизации этих рисков и проблем. Если бы у вас был выбор, создавали бы вы гетерогенную среду или нет? Мотивируйте ваш ответ примерами.

> Недостатки:
> - сложность администрирования
> - необходимо наличие высококвалифицированных специалистов
> - сложность миграции и масштабирования
> - необходимость создания сложных систем мониторинга
> 
> Митигация рисков: 
> - разделение команд поддержки
> - IaaS
