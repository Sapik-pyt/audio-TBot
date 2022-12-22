import os

import cv2
import ffmpeg

# Функции для сохранения файла отправленного пользователем
def save_file(bot, type, file_id, user_id):
    link_file = bot.get_file(file_id)
    file_id, file_path = link_file.file_id, link_file.file_path
    file = bot.download_file(file_path)

    save_path = f'{os.path.join(user_id, file_id, type)}'
    with open(save_path, 'wb') as path:
        path.write(file)
    if type == 'audio':
        audio_converter(save_path)
    elif type == 'photo':
        if check_users_photo(save_path):
            os.remove(save_path)
            return (False, '')
    return (True, save_path)

# Конверт формата в 16kHz
def audio_converter(path):
    pathes = ffmpeg.input(path)
    out_pathes = ffmpeg.output(pathes, f'{path}.wav', ar=16000)
    ffmpeg.run(out_pathes)
    os.remove(path)

# Распознавание лица на фото
def check_users_photo(path):
    cascade_face = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_alt.xml"
    )
    photo = cv2.imread(path)
    color_photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    face = cascade_face.detectMultiScale(color_photo, 1.3, 5)
    if len(face) != 0:
        return True
    return False
