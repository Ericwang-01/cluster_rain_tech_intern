# encoding:utf-8
import logging

# 创建一个日志对象
logger = logging.getLogger()

# 设置日志级别为DEBUG
logger.setLevel(logging.DEBUG)

# 创建一个文件处理器
file_handler = logging.FileHandler('mylog.log', encoding='utf-8')

# 设置文件处理器的日志级别为INFO
file_handler.setLevel(logging.INFO)

# 设置日志输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 给日志对象添加文件处理器
logger.addHandler(file_handler)

# 输出日志
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

