# AMPI

Реализация многопользовательской системы загрузки и выгрузки небольших файлов.
1. Пользователь взаимодействует с системой через единый шлюз доступа по протоколу HTTP.
2. Система состоит из нескольких отдельных сервисов (БД для пользователей, файлов и отчетов). 
3. У каждого сервиса своя БД.
4. Сервисы взаимодействуют асинхронно передавая и получая события об изменениях через шину.
5. Падение одного сервиса не должно приводить к недоступности всей системы.

## Локальный запуск проекта

### Начало работы


#### Предварительная установка зависимостей.

1. ```python -m venv venv``` - создание виртуальной среды.
2. ```source venv/bin/activate``` - активация созданного пространства для Linux, MacOS. Для Windows команда выглядит так:
 
   ```.\venv\Scripts\activate```
3. ```pip install -r requirements.txt```  - установка зависимостей.


Перед началом работы нужно запустить docker-compose для запуска контейнеров, на котором находятся сервисы:

```docker-compose -f docker-compose.local.up```

#### Подключение к PostgreSQL:
Подключаемся к PostgeSQL (datagrip, инструменты ide, иные инструменты).

К трем БД по 5495, 5496, 5497 портам. Также необходимо прописать необходимые данные в переменных окружения.

#### Применение миграций:
Находясь в виртуальном окружении, выполняем:

```python manage.py migrate```

```python manage.py migrate files --database=files```

```python manage.py migrate reports --database=reports```

#### Создание супер-пользователя и запуск проекта:

Выполняем:

```python manage.py createsuperuser```

Запускаем проект:

```python manage.py runserver```

