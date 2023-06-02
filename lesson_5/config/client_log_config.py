import logging
import os
from lesson_3.common.variables import LOGGING_LEVEL

# Подготовка имени файла для логирования
PATH = "../logs/client"
PATH = os.path.join(PATH, 'client.log')

#Файл логов
FILE_HANDLER = logging.FileHandler(PATH, encoding='utf8')

#Формат сообщения
FORMATTER = logging.Formatter("%(asctime)-25s %(levelname)-10s %(filename)-10s %(message)s")
FILE_HANDLER.setFormatter(FORMATTER)

#Cоздание логгера
LOG = logging.getLogger('client')
LOG.setLevel(LOGGING_LEVEL)
LOG.addHandler(FILE_HANDLER)

#Отладка
if __name__ == '__main__':
    LOG.critical('Критическая ошибка')
    LOG.error('Ошибка')
    LOG.warning('Предупреждение')
    LOG.info('Информационное сообщение')
    LOG.debug('Отладочная информация')
