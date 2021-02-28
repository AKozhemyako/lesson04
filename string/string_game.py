# reading
# The programm make reading from *txt file
print('Открываю файл ssh.txt: ')
text_file = open('ssh.txt', 'r')

print('\nЧитаю некоторые символы из файла')
print(text_file.read(1))
print(text_file.read(4))
print(text_file.read(10))

print('\nЧитаю остальную часть файла')
print(text_file.read())
print('Закрываю файлю')
text_file.close()
print('Файл закрыт.')
print('Открываю файл ssh, ставлю кодировку utf-8, если будут русские буквы')
text_file = open('ssh.txt', 'r', encoding='utf-8')
print('Читаю строки с 1 по 5 открыторго файла, и закрываю файл')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()
print('Открываю файл ssh.txt.')
text_file = open('ssh.txt', 'r', encoding='utf-8')
print('Читаю строки с 1 открыторго файла')
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
print('и закрываю файл...')
text_file.close()
print('Перебор файла по строчно.')
text_file = open('ssh.txt', 'r', encoding='utf-8')
for line in text_file:
    print(line)
text_file.close()
input('\n\nНажмите Enter, чтобы выйти.')


