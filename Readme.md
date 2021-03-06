#Создание веб-приложения с помощью Flask в Python 3
https://github.com/vitaliy-tymashkov/SimpleUi

Введение
Flask — это небольшой и легкий веб-фреймворк, написанный на языке Python, предлагающий полезные инструменты и функции для облегчения процесса создания веб-приложений с использованием Python. Он обеспечивает гибкость и является более доступным фреймворком для новых разработчиков, так как позволяет создать веб-приложение быстро, используя только один файл Python. Flask — это расширяемая система, которая не обязывает использовать конкретную структуру директорий и не требует сложного шаблонного кода перед началом использования.

В рамках этого обучающего руководства вы будете использовать инструментарий Bootstrap, чтобы сделать ваше приложение визуально привлекательным. Bootstrap поможет вам включить в ваше веб-приложение быстрые веб-страницы, чтобы приложение можно было использовать на мобильных браузерах без написания для этого собственных кодов HTML, CSS и JavaScript. Инструментарий дает возможность изучить работу Flask.

Flask использует механизм шаблонов Jinja для динамического создания HTML-страниц с использованием знакомых понятий в Python, таких как переменные, циклы, списки и т. д. Вы будете использовать эти шаблоны в рамках этого проекта.

С помощью этого обучающего руководства вы создадите небольшой веб-блог с использованием Flask и SQLite в Python 3. Пользователи приложения могут видеть все посты в вашей базе данных и нажимать на заголовки постов для просмотра их содержания. Кроме того, присутствует возможность добавлять новый пост в базу данных и редактировать или удалять существующий пост.
[Link](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-ru)

Before starting App.py database.db should be created. Run init_db.py!


[Как установить Flask на Windows?](https://coderoad.ru/17917254/%D0%9A%D0%B0%D0%BA-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C-Flask-%D0%BD%D0%B0-Windows)



[Docker](https://www.youtube.com/watch?v=QF4ZF857m44&t=1899s)

[dockerize-your-flask-application](https://runnable.com/docker/python/dockerize-your-flask-application)

pip -install -r requirements.txt


+++++++++++++++++
##To build an image

docker build -t ocr01:latest .
&&\

docker run -d --name ocr01c -p 8080:57777 ocr01 &&\


docker exec -it ocr01c /bin/bash



###Other commands
docker stop ocr01c && docker rm ocr01c && docker rmi ocr01


nc -zv localhost 57777


nc -zv 172.17.0.2 57777
response: bd6f20995939 [172.17.0.2] 57777 (?) open

###Links
IDEA - http://localhost:57777/
Docker - http://localhost:8080/