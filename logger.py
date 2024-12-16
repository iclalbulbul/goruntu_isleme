from loguru import logger

log_settings = [
    {
        "filename": "debug.log",
        "level": "DEBUG",
        "rotation": "1 MB",
        "retention": "7 days",
        "compression": "zip",
        "format":  "{time} {level} {file} {line} {message}",
    },

    {
       "filename": "critical.log",
        "level": "CRITICAL",
        "rotation": "1 week",
        "retention": "30 day",
        "compression": None,
        "format": "{time} {level} {message}"

    },
]

# log ayarlarını uygulama

def setup_logger():
    for setting in log_settings:
        logger.add(
            setting["filename"],
            level=setting["level"],
            rotation=setting["rotation"],
            retention=setting["retention"],
            compression=setting["compression"],
            format=setting["format"],
        )

# loggerı ayarlama
setup_logger()

logger.debug("bu bir DEBUG mesajıdır")
logger.info("bu bir INFO mesajıdır")
logger.error("bu bir ERROR mesajıdır")
logger.critical("bu bir CRITICAL mesajıdır")




