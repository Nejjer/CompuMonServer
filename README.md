# CompuMonServer

Серверная часть для проекта CompuMon - мониторинг за состоянием ПК

Этот репозиторий содержит два каталога — **win** и **linux**, предназначенные для соответствующих операционных систем. В каждом из них находится серверное приложение, написанное с использованием FastAPI. Приложение получает информацию о системе (например, загрузка процессора, температура, память) и предоставляет её через API.

## Структура репозитория

- **win/** — Код для запуска сервера на операционной системе Windows.
- **linux/** — Код для запуска сервера на операционной системе Linux.

## Требования

Перед запуском убедитесь, что у вас установлен Python, а также все необходимые зависимости.

### Шаги для установки

1. Установите **Python**. Если у вас его еще нет, загрузите и установите Python с [официального сайта](https://www.python.org/downloads/).

2. Установите зависимости с помощью команды:

    ```bash
    pip install -r requirements.txt
    ```

    В файле `requirements.txt` указаны все необходимые библиотеки, включая FastAPI и другие зависимости для работы с системой.

### Настройка и запуск сервера на Windows

1. Перейдите в каталог **win**:

    ```bash
    cd win
    ```

2. Создайте файл `.env` в этой папке и укажите настройки для вашего сервера. Пример файла `.env`:

    ```env
    HOST=0.0.0.0
    PORT=5000
    ```

3. Запустите сервер(На Windows нужно запускать с правами админа):

    ```bash
    python server.py
    ```

Теперь ваш сервер будет работать на Windows, и вы сможете получить доступ к API, например, по адресу `http://0.0.0.0:5000/api/getPcStatus`.

### Настройка и запуск сервера на Linux

1. Перейдите в каталог **linux**:

    ```bash
    cd linux
    ```

2. Создайте файл `.env` в этой папке и укажите настройки для вашего сервера. Пример файла `.env`:

    ```env
    HOST=0.0.0.0
    PORT=5000
    ```

3. Запустите сервер:

    ```bash
    python server.py
    ```

Теперь ваш сервер будет работать на Linux, и вы сможете получить доступ к API, например, по адресу `http://0.0.0.0:5000/api/getPcStatus`.

### Примечания

- Для корректной работы на Windows необходимо наличие библиотеки `pythonnet` для взаимодействия с .NET компонентами.
- Для Linux код использует команды `inxi` для получения информации о системе, убедитесь, что эта утилита установлена. Для установки `inxi` на Linux выполните команду:
  ```bash
  sudo apt-get install inxi
  ```
