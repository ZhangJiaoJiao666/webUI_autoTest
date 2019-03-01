import logging
import os.path
#创建一个logger对象
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


#使用handler 输出日志信息
ch=logging.StreamHandler()
fh=logging.FileHandler('./logs')#向控制台输出日志信息
logger.addHandler(ch)
logger.addHandler(fh)

#Formatter 对象设置日志信息最后的规则、结构和内容，默认的时间格式 为%Y-%m-%d %H:%M:%S
fomatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
ch.setFormatter(fomatter)

logger.info("info日志信息")
logger.debug("debug日志信息")
logger.warning("warning日志信息")
logger.error("error日志信息")








