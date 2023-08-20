from os import path

from vyper import v as config


class CfgPath:
    SERVER_ADDRESS = 'server.address'
    SERVER_PORT = 'server.port'


class Options:
    SERVER_ADDRESS = '--server_address'
    SERVER_PORT = '--server_port'


class Config:
    def __init__(self, consts=CfgPath):
        self.ROOT_DIR = path.abspath(path.join(__file__, '../../'))
        self.consts = consts
        self.init_config()

    def init_config(self):
        config_name = 'config'
        config.set_config_name(config_name)
        config.set_config_type('yaml')
        config.add_config_path(self.ROOT_DIR)
        config.read_in_config()

    @staticmethod
    def get_raw_value(key_path):
        return config.get(key_path)
