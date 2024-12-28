try:
    file = open('1_print.py')
except OSError as err:
    print('File not found' + str(err))
    print('Unexpected error')
else:
    print(file.read())
    file.close()
