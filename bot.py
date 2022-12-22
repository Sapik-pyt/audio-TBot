import os

import telebot
from dotenv import load_dotenv

import utils
from db import Photo, User, Voice, sessia

load_dotenv()

bot = telebot.TeleBot('BOT_API')

# Создание пользователя или поиск его в БД
def get_of_create_user(sessia, user_id, username):
    user = sessia.query(User).filter_by(id=user_id).first()
    if user:
        return user
    else:
        user = User(id=user_id, name=username)
        sessia.add(user)
        return user


if not (os.path.isdir(os.path.join('audio'))):
    os.mkdir(os.path.join('audio'))
if not (os.path.isdir(os.path.join('photo'))):
    os.mkdir(os.path.join('photo'))

# Обработка голосого сообщения
@bot.message_handler(content_types=['voice'])
def audio_process(message):
    voice_id = message.voice.file.id
    username, user_id = message.from_user.username, message.from_user.id

    get_of_create_user(sessia, user_id, username)
    null, path = utils.save_file(bot, 'audio', voice_id, user_id)
    sessia.add(Voice(id=voice_id, path=path, user_id=user_id))
    sessia.commit()
    bot.reply_to(message, 'Аудиозапись сохранена')

# Распознание лица, добавление фото при положительном результате
@bot.message_handler(content_types=['photo'])
def photo_process(message):
    photo_id = message.photo[2].file_id
    user_id, username = message.from_user.id, message.from_user.username

    get_of_create_user(sessia, user_id, username)
    status, path = utils.save_file(bot, 'photo', photo_id, user_id)
    if status:
        sessia.add(Photo(id=photo_id, path=path, user_id=user_id))
        sessia.commit()
        bot.reply_to(message, 'Фото загружено')
    else:
        bot.reply_to(message, 'На фотографии нет лица')


bot.polling()
