import subprocess
import chardet

#Яндекс
ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

#Youtube
ARGS = ['ping', 'youtube.com']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))