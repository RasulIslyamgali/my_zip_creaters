import zipfile
'''Этот код была создана лишь для проверки работы встроенного модуля python zipfile
Если вы хотите воспользоваться им, надо будет добавить возможность сохранения файлов
внутри папок(в случае архиваирования папки. Это сделать не сложно.
Для этого можете воспользоваться if os.path.isfile(file): и дальше уже работать с этой информацией.'''

# выбираем имя архива
archive = zipfile.ZipFile(r'C:\Users\Admin\Desktop\Programming\test_save_folder\my_archive.zip', mode='w')

try:
    archive.write(r'C:\Users\Admin\Desktop\Programming\test_folder')
    archive.write(r'C:\Users\Admin\Desktop\Programming\test2.txt')
    print('Архивировано.')
    archive.close()
finally:
    pass


