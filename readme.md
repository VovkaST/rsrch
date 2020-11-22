Приложение для создания анкет
==

#### Установка
Создаем каталог приложения и переходим в него:
```commandline
user@dev-note:~$ cd ~/
user@dev-note:~$ mkdir develop
user@dev-note:~$ cd develop/
user@dev-note:~/develop$ 
```

Клонируем репозиторий
```commandline
user@dev-note:~/develop$ git clone https://github.com/VovkaST/rsrch.git
```

Создаем виртуальное окружение `.venv` в текущем каталоге:
```commandline
user@dev-note:~/develop$ python3 -m venv .venv
```

Активируем его и устанавливаем зависимости:
```commandline
user@dev-note:~/develop$ source .venv/bin/activate 
(.venv) user@dev-note:~/develop/.venv/bin$ cd ../..
(.venv) user@dev-note:~/develop$ pip3 -r install requirements.txt
```

#### Настройка, тестовые данные и запуск
Все настройки указаны в `settings.py` кроме:
```python
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
```
Константы необходимы для отправки писем (используется smtp сервер mail.ru) и должны быть размещены в файле 
`settings_local.py` в одном каталоге с основным файлом настроек.

Восстанавливаем фикстуры:
```commandline
(.venv) user@dev-note:~/develop$ python3 manage.py loaddata fixtures/datadump.json
```

И запускаем сервер:
```commandline
(.venv) user@dev-note:~/develop$ python3 manage.py runserver
```


#### Механика
Предварительно создаются Форма опроса с набором полей, Шаблон документа для форматирования результатов и Страница 
завершения для перенаправления пользователя по ссылке из письма. После этого создается Анкета с привязкой всех 
перечисленных объектов.

На уникальной странице анкеты генерируется указанная форма со всеми связями, после нажатия отправки формы и при условии 
заполнения всех требуемых полей, пользователю из пары "хэш заполненных данных" + "ссылка на страницу заполнения анкеты" 
генерируется уникальная ссылка, которая отправляется на емайл, используя Шаблон документа. При переходе по ссылке, 
пользователю отображается страница завершения. Также представляется возможность скачать результаты в виде pdf-файла.
