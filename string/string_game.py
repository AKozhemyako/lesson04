# reading
# The programm make reading from *txt file
print('Open end close file')
text_file = open('ssh.txt', 'r')
text_file.close()
print('\nread file by symbol`s.')
text_file = open('ssh.txt', 'r')
print(text_file.read())
text_file.close()
print('\nFile is read and close.')

