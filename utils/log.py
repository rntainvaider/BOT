import logging


def setup_logging(log_file: str = "bot.log"):
    """
    Настройка логирования для записи в файл и вывода в терминал.

    :param log_file: Имя файла для записи логов.
    """
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


# Вызов функции настройки логирования
setup_logging()
