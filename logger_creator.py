import logging
import os


class LoggerCreator:
    def __init__(self, log_file_name='sample-log-file-name.log'):
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.INFO)
        self._log_file_name = log_file_name

    def create(self):
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.INFO)

        logging_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self._add_file_handler(logging_formatter)
        self._add_stream_handler(logging_formatter)

        return self._logger

    def _add_file_handler(self, logging_formatter):
        log_dir = 'logs'
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, self._log_file_name)

        file_handler = logging.FileHandler(log_file, mode='a')
        file_handler.setFormatter(logging_formatter)

        self._logger.addHandler(file_handler)

    def _add_stream_handler(self, logging_formatter):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging_formatter)

        self._logger.addHandler(stream_handler)
