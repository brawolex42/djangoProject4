# Python Advanced: Домашнее задание 7
#
# Вам необходимо самостоятельно создать Django проект и добавить его в Git.
#
# Создание проекта:
#
# Создайте новый Python проект.
#
# Установите фреймворк Django.
#
# Создайте структуру Django проекта с помощью команды в консоли.
#
# Настройка переменных окружения:
#
# Создайте файл .env в корне проекта и добавьте переменные SECRET_KEY, DEBUG и ALLOWED_HOSTS.
#
# Установите библиотеку django-environ для работы с переменными окружения.
#
# Считайте переменные SECRET_KEY, DEBUG и ALLOWED_HOSTS из .env файла в settings.py.
#
# Настройка базы данных:
#
# Добавьте в .env файл настройки для подключения к MySQL.
#
# Реализуйте в settings.py возможность выбора между SQLite и MySQL в зависимости от переменной MYSQL в .env файле.
#
# Создание и регистрация приложения:
#
# Создайте новое приложение в вашем проекте Django.
#
# Зарегистрируйте приложение в настройках проекта (settings.py).
#
# Реализация представления и маршрута:
#
# Определите простое представление, которое будет возвращать заголовком текст "Hello, <your_name>".
#
# Определите URL-маршрут к вашему представлению внутри приложения.
#
# Подключите маршруты вашего приложения к основному файлу urls.py проекта.
#
# Тестирование:
#
# Запустите локальный сервер и перейдите по созданному URL адресу для проверки корректности реализации.
#
# Фиксация зависимостей:
#
# Зафиксируйте текущие версии всех зависимостей в файле requirements.txt.
#
# Git
#
# Запуште проект в гит репозиторий и прикрепите как решение ссылку на него.



from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, False), MYSQL=(bool, False))
environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "greet",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hw7_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hw7_project.wsgi.application"

if env.bool("MYSQL", False):
    import pymysql
    pymysql.install_as_MySQLdb()
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": env("MYSQL_DB"),
            "USER": env("MYSQL_USER"),
            "PASSWORD": env("MYSQL_PASSWORD"),
            "HOST": env("MYSQL_HOST", default="localhost"),
            "PORT": env.int("MYSQL_PORT", default=3306),
            "OPTIONS": {"charset": "utf8mb4"},
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Berlin"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
