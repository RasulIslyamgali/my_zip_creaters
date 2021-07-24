import os
import time

# в список собираем файлы и папки/каталоги, которых будем архивировать
# r я ставил, чтобы python не ругалась на слэши, когда будем указывать путь
# пример указывания папок и файлов для сохранения
# OS Windows C:\Users\Admin\Desktop\Programming\test_for_zip
# OS Windows C:\Users\Admin\Desktop\Programming\test_for_zip_file_2.txt
# можете указывать сколько угодно файлов и папок
my_files = [r'C:\Users\Admin\Desktop\Programming\test_folder',
            r'C:\Users\Admin\Desktop\Programming\test2.txt']

# указывайте папку, в котором хотите создать zip файл
# Пример указвания директории для сохранения zip файла
# OS Windows C:\Users\Admin\Desktop\Programming\test_folder_to_save_zip
folder_for_save = r'C:\Users\Admin\Desktop\Programming\test_save_folder'

# создаем подкаталог, для хранения zip файлов. имя его будет создаваться из сегоднящней даты
# os.sep нужна для указывания разделителя, исходя из ОС.
today_folder = folder_for_save + os.sep + time.strftime('%Y%m%d')

# для имени архива используем текущее время
now_file = time.strftime('%H%M%S')

# если каталога для хранения zip файла нету, то создаем его
if not os.path.exists(today_folder):
    os.mkdir(today_folder)
    print('Каталог для хранения zip файла успешно создан')

# комментарии к сохраняемому архиву. необязательна
comment = input('Можете ввести комментарий:\n')
if len(comment) == 0:
    # в случае не введения комментария, просто объединяем путь и имя zip файла
    zip_folder_file = today_folder + os.sep + now_file
else:
    zip_folder_file = today_folder + os.sep + now_file + '_' + \
        comment.replace(' ', '_') + '.zip'

# создаем zip команду
zip_command = "zip -qr {0} {1}".format(zip_folder_file, " ".join(my_files))

if __name__ == '__main__':
    if os.system(zip_command) == 0:
        print(f'Архивация в zip файл прошла успешно. Ваш файл сохранен по директории:\n{zip_folder_file}')
    else:
        print('Возникли проблемы. Архивация не была выполнена.')