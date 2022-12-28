### Как запустить проект «API для Yatube»:

Используемые технологии:
> Python

> Django

> DRF

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Rashid-creator-droid/api_final_yatube.git
```


Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

Полная документация по эндпоинтам и примерам запросов к API по ссылке :

```
http://127.0.0.1:8000/redoc/
```