import logging

logFormat = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s")

logging.basicConfig(level=logging.INFO, datefmt="%Y-%m-%d %H:%M")

cLogger = logging.getLogger("CST-LOG")
cLogger.propagate = False

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

errorHandler = logging.FileHandler("logs.log")
errorHandler.setLevel(logging.INFO)

cLogger.addHandler(errorHandler)
cLogger.addHandler(consoleHandler)

consoleHandler.setFormatter(logFormat)
errorHandler.setFormatter(logFormat)
