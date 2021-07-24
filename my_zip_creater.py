import os
import time

# в список собираем файлы и папки/каталоги, которых будем архивировать
# r я ставил, чтобы python не ругалась на слэши, когда будем указывать путь
# пример указывания папок и файлов для сохранения
# OS Windows C:\Users\Admin\Desktop\Programming\test_for_zip
# OS Windows C:\Users\Admin\Desktop\Programming\test_for_zip_file_2.txt
# можете указывать сколько угодно файлов и папок
my_files = [r'',
            r'']

# указывайте папку, в котором хотите создать zip файл
# Пример указвания директории для сохранения zip файла
# OS Windows C:\Users\Admin\Desktop\Programming\test_folder_to_save_zip
folder_for_save = r''

# эта строка будет использоваться для zip команды. в конце будут указана название файла.
# в данном случае оно состоит из времени, в котором zip файл была создана
# os.sep нужна для указывания разделителя, исходя из ОС.
name_to_zip_file = folder_for_save + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# создаем zip команду
# если убрать параметр r, то при архивации не будут сохранены подкаталоги папок
zip_command = "zip -qr {0} {1}".format(name_to_zip_file, " ".join(my_files))

if __name__ == '__main__':
    if os.system(zip_command) == 0:
        print(f'Архивация в zip файл прошла успешно. Ваш файл сохранен по директории:\n{name_to_zip_file}')
    else:
        print('Возникли проблемы. Архивация не была выполнена.')
