import logging.handlers
import os
from lesson_3.common.variables import LOGGING_LEVEL

#Подготовка имени файла для логирования
PATH = "../logs/server"
PATH = os.path.join(PATH, 'server.log')

#Файл логов
FILE_HANDLER = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')

#Формат сообщения
FORMATTER = logging.Formatter("%(asctime)-25s %(levelname)-10s %(filename)-10s %(message)s")
FILE_HANDLER.setFormatter(FORMATTER)

#Cоздание логгера
LOG = logging.getLogger('server')
LOG.setLevel(LOGGING_LEVEL)
LOG.addHandler(FILE_HANDLER)

#Отладка
if __name__ == '__main__':
    LOG.critical('Критическая ошибка')
    LOG.error('Ошибка')
    LOG.warning('Предупреждение')
    LOG.info('Информационное сообщение')
    LOG.debug('Отладочная информация')
