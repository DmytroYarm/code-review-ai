import logging

# Настройки логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Пример использования логирования
def log_message(message: str):
    logger.info(f"Logging message: {message}")
