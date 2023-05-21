with open('test_file.txt') as codedFile:
    print(f'Кодировка файла: {codedFile.encoding}')
    for line in codedFile:
        # преобразуем содержимое в utf-8
        encd_line = line.encode('utf-8')
        # декодируем содержимое
        dcd_line = encd_line.decode('utf-8')
        print(dcd_line)