
Audio-bot


1)Сохранять аудиосообщения из диалогов в базу данных (СУБД или на диск) по идентификаторам пользователей.
2)Конвертирует все аудиосообщения в формат wav с частотой дискретизации 16kHz Формат записи: uid —> [audio_message_0, audio_message_1, ..., audio_message_N].
3)Определяет есть ли лицо на отправляемых фотографиях или нет, сохраняет только те, где оно есть

Запуск проекта 
- Клонировать репозиторий и перейти в него в командной строке.
- Установите и активируйте виртуальное окружение c учетом версии Python 3.9 (выбираем python не ниже 3.9):

```bash
py -3.9 -m venv venv
```

```bash
source venv/Scripts/activate
```

- Затем нужно установить все зависимости из файла requirements.txt

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```
```
Запустить бота: bot.py
```
