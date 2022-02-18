"""
    File name: logger_parse.py
    Description: This file could read json logging file and config log system

    Author: Botian Lan
    Time: 2022/01/29
"""
import logging.config
import logging
import pathlib

from utils_json import *


def logger_parser(config_file_path):
    """
        This function is a node between json structure and dict structure.
    :param config_file_path:
    :return: A dict data that json file contained.
    """
    config_file_path = pathlib.Path(config_file_path)

    if config_file_path.is_file():
        logger_config = read_json(config_file_path)
        logging.config.dictConfig(logger_config)
        return logger_config

    else:
        raise FileNotFoundError("Object file '{}' is not found!".format(config_file_path))


def logger_packer(config_file_path):
    """
        By using logger_parser, this function can directly parse log_config.json and generate a list which
    consists of loggers that json file has.
    :param config_file_path:
    :return: exist loggers name cluster
    """
    names = []
    logger_json = logger_parser(config_file_path)
    loggers_cluster = logger_json['loggers']
    for name, value in loggers_cluster.items():
        names.append(name)
    return names


if __name__ == '__main__':
    loggers = logger_packer('log_config.json')
    print(loggers)

    a = 3

